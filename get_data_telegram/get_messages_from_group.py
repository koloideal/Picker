import re
from configparser import ConfigParser
import json
from telethon.sync import TelegramClient
from dateutil import tz
import dateutil.parser


config: ConfigParser = ConfigParser()
config.read("secret_data/config.ini")


api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']


client = TelegramClient('session', int(api_id), api_hash)


async def get_messages_from_group(url, limit):

    await client.start()

    channel = await client.get_entity(url)

    messages = await client.get_messages(channel, limit=int(limit))

    users_id = []

    for x in messages:

        try:

            users_id.append(x.to_dict()['from_id']['user_id'])

        except KeyError:

            continue

    all_need_users = []

    for ids in set(users_id):

        user = await client.get_participants(ids)

        all_need_users.append(user[0].to_dict())

    dict_with_all_data = {}

    for user in all_need_users:

        dict_with_all_data[user['id']] = {

            'username': user['username'],
            'first_name': user['first_name'],
            'phone': user['phone']

        }

    to_time_zone = tz.gettz('Europe/Minsk')

    all_messages = []

    for message in messages:

        msg_to_dict = message.to_dict()

        date_time_iso = msg_to_dict['date'].isoformat()
        date_time_obj = dateutil.parser.isoparse(date_time_iso)
        date_time_obj = date_time_obj.astimezone(to_time_zone)

        result_date = date_time_obj.strftime('%m-%d-%Y %H:%M:%S')

        try:

            user_id = msg_to_dict['from_id']['user_id']

            if user_id in dict_with_all_data.keys():

                all_messages.append({

                    'date': result_date,
                    'message': msg_to_dict['message'],
                    'username': dict_with_all_data[user_id]['username'],
                    'first_name': dict_with_all_data[user_id]['first_name'],
                    'phone': dict_with_all_data[user_id]['phone']

                })

            else:

                user = await client.get_participants(message.from_id)

                need_user = user[0]

                all_messages.append({

                    'date': result_date,
                    'message': msg_to_dict['message'],
                    'username': need_user.username,
                    'first_name': need_user.first_name,
                    'phone': need_user.phone

                })

        except KeyError:

            continue

    await client.disconnect()

    channel_title = re.sub(r'[^a-zA-Zа-яА-Я0-9]', '_', channel.title)

    with open(f'messages_of_groups_to_json/{channel_title}.json', 'w', encoding='utf8') as file:

        json.dump({channel_title: all_messages}, file, indent=4, ensure_ascii=False)

    return channel_title
