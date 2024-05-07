import re
from configparser import ConfigParser
from telethon.sync import TelegramClient
from aiogram.types import Message
import json
from telethon.errors.rpcerrorlist import InviteHashExpiredError, InviteHashEmptyError
from telethon.tl.functions.messages import CheckChatInviteRequest
from telethon.tl.types import ChatInvite

config: ConfigParser = ConfigParser()

config.read('secret_data/config.ini')

api_id: str = config.get('Telegram', 'api_id')
api_hash: str = config.get('Telegram', 'api_hash')


client: TelegramClient = TelegramClient('session', int(api_id), api_hash)


async def get_users_from_private_groups(message: Message) -> str | None:

    await client.start()

    try:

        link: str = message.text.split('+')[1]

        channel: ChatInvite | None = await client(CheckChatInviteRequest(hash=link))

        users: list = [user.__dict__ for user in channel.participants]

    except (InviteHashExpiredError, InviteHashEmptyError):

        await client.disconnect()

        await message.answer('Invalid link')

        return

    else:

        await client.disconnect()

    all_users_details: list = []

    for participant in users:

        all_users_details.append({

            "id": participant['id'],
            "first_name": participant['first_name'],
            "last_name": participant['last_name'],
            "username": participant['username'],
            "phone": participant['phone'],
            "is_bot": participant['bot']

        })

    private_group_title: str = re.sub(r'[^a-zA-Zа-яА-Я0-9]', '_', channel.title)

    with open(f'content/{private_group_title}.json', 'w', encoding='utf8') as file:

        json.dump({private_group_title: all_users_details}, file, indent=4, ensure_ascii=False)

    return private_group_title
