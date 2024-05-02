import re
from configparser import ConfigParser
from telethon.sync import TelegramClient
from telethon import functions
from aiogram.types import Message
import json
from telethon.errors.rpcerrorlist import InviteHashExpiredError, InviteHashEmptyError

config: ConfigParser = ConfigParser()

config.read('secret_data/config.ini')

api_id: str = config.get('Telegram', 'api_id')
api_hash: str = config.get('Telegram', 'api_hash')


async def get_users_from_private_groups(message: Message):

    client: TelegramClient = TelegramClient('session', int(api_id), api_hash)

    await client.start()

    try:

        link = message.text.split('+')[1]

        channel = await client(functions.messages.CheckChatInviteRequest(hash=link))

        users = [user.__dict__ for user in channel.participants]

    except (InviteHashExpiredError, InviteHashEmptyError):

        await client.disconnect()

        await message.answer('Некорректная ссылка')

        return

    else:

        await client.disconnect()

    private_group_title = re.sub(r'[^a-zA-Zа-яА-Я0-9]', '_', channel.title)

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

    with open(f'users_of_private_groups_to_json/{private_group_title}.json', 'w', encoding='utf8') as file:

        json.dump({private_group_title: all_users_details}, file, indent=4, ensure_ascii=False)

    return private_group_title
