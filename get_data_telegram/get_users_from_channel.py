import os

from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
import configparser
import json

config = configparser.ConfigParser()
config.read('secret_data/config.ini')

api_id = config.get('Telegram', 'api_id')
api_hash = config.get('Telegram', 'api_hash')


async def get_users_from_channel(channel_name):

    client = TelegramClient('session', int(api_id), api_hash)

    await client.start()

    channel = await client.get_entity(channel_name)

    channel_title = channel.title.replace(' ', '_').replace('/', '').replace('\\', '')

    offset = 0
    limit = 100
    all_users = []

    while True:

        result = await client(GetParticipantsRequest(

            channel=channel,
            filter=ChannelParticipantsSearch(''),
            offset=offset,
            limit=limit,
            hash=0

        ))

        users = result.users

        all_users.extend(user.__dict__ for user in users)

        if len(users) < limit:
            break

        offset += limit

    await client.disconnect()

    result = []

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
