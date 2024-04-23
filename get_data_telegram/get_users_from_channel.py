import asyncio
import re

from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch, Channel
from configparser import ConfigParser
import json
from telethon.errors.rpcerrorlist import ChatAdminRequiredError

config: ConfigParser = ConfigParser()
config.read('secret_data/config.ini')

api_id: str = config.get('Telegram', 'api_id')
api_hash: str = config.get('Telegram', 'api_hash')


async def get_users_from_channel(channel_name):

    client: TelegramClient = TelegramClient('session', int(api_id), api_hash)

    await client.start()

    channel: Channel = await client.get_entity(channel_name)

    channel_title = re.sub(r'[^a-zA-Zа-яА-Я0-9]', '_', channel.title)

    offset: int = 0
    limit: int = 100
    all_users: list = []

    while True:

        try:

            result: client = await client(GetParticipantsRequest(

                channel=channel,
                filter=ChannelParticipantsSearch(''),
                offset=offset,
                limit=limit,
                hash=0

            ))

        except ChatAdminRequiredError:

            await client.disconnect()

            return '!ChatAdminRequiredError'

        except ValueError:

            await client.disconnect()

            return '!ValueError'

        else:

            users: list = result.users

            all_users.extend(user.__dict__ for user in users)

            if len(users) < limit:

                break

            offset += limit

    await client.disconnect()

    result: list = []

    for user in all_users:

        result.append({

            'id': user['id'],
            'first_name': user['first_name'],
            'last_name': user['last_name'],
            'username': user['username'],
            'phone': user['phone'],
            'is_bot': user['bot']

        })

    with open(f'users_of_channels_to_json/{channel_title}.json', 'w', encoding='utf8') as file:

        file.write('{}')

    with open(f'users_of_channels_to_json/{channel_title}.json', 'r+', encoding='utf8') as file:

        file_data: json = json.load(file)

        file_data[channel_title]: json = result

        file.seek(0)

        json.dump(file_data, file, indent=4, ensure_ascii=False)

    return channel_title
