import re
from configparser import ConfigParser
from telethon.sync import TelegramClient
from telethon.tl.types import Channel
from aiogram.types import Message
import json
from telethon.errors.rpcerrorlist import ChatAdminRequiredError
from telethon.helpers import TotalList

config: ConfigParser = ConfigParser()

config.read('secret_data/config.ini')

api_id: str = config.get('Telegram', 'api_id')
api_hash: str = config.get('Telegram', 'api_hash')


client: TelegramClient = TelegramClient('session', int(api_id), api_hash)


async def get_users_from_groups(message: Message) -> str | None:

    await client.start()

    try:

        channel: Channel = await client.get_entity(message.text)

        all_users: TotalList = await client.get_participants(message.text)

    except ChatAdminRequiredError:

        await client.disconnect()

        await message.answer('You must be the owner or admin of this channel')

        return

    except ValueError:

        await client.disconnect()

        await message.answer('Invalid link')

        return

    else:

        await client.disconnect()

    all_users_details: list = []

    for participant in all_users:

        all_users_details.append({

            "id": participant.id,
            "first_name": participant.first_name,
            "last_name": participant.last_name,
            "username": participant.username,
            "phone": participant.phone,
            "is_bot": participant.bot

        })

    channel_title: str = re.sub(r'[^a-zA-Zа-яА-Я0-9]', '_', channel.title)

    with open(f'content/{channel_title}.json', 'w', encoding='utf8') as file:

        json.dump({channel_title: all_users_details}, file, indent=4, ensure_ascii=False)

    return channel_title
