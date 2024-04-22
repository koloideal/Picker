import configparser
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
import json

config = configparser.ConfigParser()

config.read('secret_data/config.ini')

api_id = config.get('Telegram', 'api_id')
api_hash = config.get('Telegram', 'api_hash')

client = TelegramClient('session', int(api_id), api_hash)


async def get_users_from_groups(message):

    offset_user = 0
    limit_user = 100

    all_participants = []
    filter_user = ChannelParticipantsSearch('')

    await client.start()

    while True:

        participants = await client(GetParticipantsRequest(message, filter_user, offset_user, limit_user, hash=0))

        if not participants.users:
            break

        all_participants.extend(participants.users)
        offset_user += len(participants.users)

    channel = await client.get_entity(message)

    await client.disconnect()

    channel_title = channel.title.replace(' ', '_').replace('/', '').replace('\\', '')

    all_users_details = []

    for participant in all_participants:

        all_users_details.append({"id": participant.id,
                                  "first_name": participant.first_name,
                                  "last_name": participant.last_name,
                                  "username": participant.username,
                                  "phone": participant.phone,
                                  "is_bot": participant.bot})

    with open(f'users_of_groups_to_json/{channel_title}.json', 'w', encoding='utf8') as file:

        file.write('{}')

    with open(f'users_of_groups_to_json/{channel_title}.json', 'r+', encoding='utf8') as file:

        file_data: json = json.load(file)

        file_data[channel_title]: json = all_users_details

        file.seek(0)

        json.dump(file_data, file, indent=4, ensure_ascii=False)

    return channel_title
