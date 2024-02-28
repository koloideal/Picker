import configparser
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
import json

config = configparser.ConfigParser()
config.read("C:\\Python_Projects\\ReAssembler\\utils\\config.ini")

api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']

client = TelegramClient(username, int(api_id), api_hash)

client.start()


async def dump_all_participants(url):

    offset_user = 0
    limit_user = 100

    all_participants = []
    filter_user = ChannelParticipantsSearch('')

    while True:

        participants = await client(GetParticipantsRequest(url, filter_user, offset_user, limit_user, hash=0))

        if not participants.users:
            break

        all_participants.extend(participants.users)
        offset_user += len(participants.users)

    all_users_details = []

    for participant in all_participants:

        all_users_details.append({"id": participant.id,
                                  "first_name": participant.first_name,
                                  "last_name": participant.last_name,
                                  "user": participant.username,
                                  "phone": participant.phone,
                                  "is_bot": participant.bot})

    print(all_users_details)

    with open('C:\\Python_Projects\\ReAssembler\\channel_users.json', 'w', encoding='utf8') as outfile:
        json.dump(all_users_details, outfile, ensure_ascii=False)


channel = client.get_entity('https://t.me/+YNI_GwHOQvwzYmJi')

with client:

    client.loop.run_until_complete(dump_all_participants(channel))
