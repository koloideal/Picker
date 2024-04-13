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


async def dump_all_participants(message):

    locate = 'C:\\Python_Projects\\ReAssembler\\channel_users.json'

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

    await client.disconnect()

    all_users_details = []

    for participant in all_participants:

        all_users_details.append({"id": participant.id,
                                  "first_name": participant.first_name,
                                  "last_name": participant.last_name,
                                  "user": participant.username,
                                  "phone": participant.phone,
                                  "is_bot": participant.bot})

    with open(locate, 'w', encoding='utf8') as outfile:
        json.dump(all_users_details, outfile, ensure_ascii=False)

    print('completed dump_all_participants')

