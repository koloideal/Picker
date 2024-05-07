import re
from configparser import ConfigParser
import json
from datetime import tzinfo
from typing import Any
from telethon.sync import TelegramClient
from dateutil import tz
import dateutil.parser
from telethon.helpers import TotalList
from telethon.tl.types import Channel


config: ConfigParser = ConfigParser()
config.read("secret_data/config.ini")


api_id: str = config['Telegram']['api_id']
api_hash: str = config['Telegram']['api_hash']


client: TelegramClient = TelegramClient('session', int(api_id), api_hash)


async def get_messages_from_group(url: str, limit: int) -> str:

    await client.start()

    channel: Channel = await client.get_entity(url)

    messages: TotalList = await client.get_messages(channel, limit=limit)

    users_id: list = []

    for x in messages:

        try:

            users_id.append(x.to_dict()['from_id']['user_id'])

        except KeyError:

            continue

    all_need_users: list = []

    for ids in set(users_id):

        user: TotalList = await client.get_participants(ids)

        all_need_users.append(user[0].to_dict())

    dict_with_all_data: dict = {}

    for need_user in all_need_users:

        dict_with_all_data[need_user['id']]: dict = {

            'username': need_user['username'],
            'first_name': need_user['first_name'],
            'phone': need_user['phone']

        }

    to_time_zone: tzinfo = tz.gettz('Europe/Minsk')

    all_messages: list = []

    for message in messages:

        msg_to_dict: dict = message.to_dict()

        date_time_iso: Any = msg_to_dict['date'].isoformat()
        date_time_obj: Any = dateutil.parser.isoparse(date_time_iso)
        date_time_obj: Any = date_time_obj.astimezone(to_time_zone)

        result_date: str = date_time_obj.strftime('%m-%d-%Y %H:%M:%S')

        try:

            user_id: int = msg_to_dict['from_id']['user_id']

            all_messages.append({

                'date': result_date,
                'message': msg_to_dict['message'],
                'username': dict_with_all_data[user_id]['username'],
                'first_name': dict_with_all_data[user_id]['first_name'],
                'phone': dict_with_all_data[user_id]['phone']

            })

        except KeyError:

            continue

    await client.disconnect()

    channel_title: str = re.sub(r'[^a-zA-Zа-яА-Я0-9]', '_', channel.title)

    with open(f'content/{channel_title}.json', 'w', encoding='utf8') as file:

        json.dump({channel_title: all_messages}, file, indent=4, ensure_ascii=False)

    return channel_title
