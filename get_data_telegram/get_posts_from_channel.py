import re
from configparser import ConfigParser
import json
from datetime import tzinfo
from typing import Any
from telethon.sync import TelegramClient
from dateutil import tz
import dateutil.parser
from telethon.tl.types import Channel
from telethon.helpers import TotalList


config: ConfigParser = ConfigParser()
config.read("secret_data/config.ini")


api_id: str = config['Telegram']['api_id']
api_hash: str = config['Telegram']['api_hash']


client: TelegramClient = TelegramClient('session', int(api_id), api_hash)


async def get_posts_from_channel(url: str, limit: int) -> str:

    await client.start()

    channel: Channel = await client.get_entity(url)

    messages: TotalList = await client.get_messages(channel, limit=limit)

    await client.disconnect()

    result_list: list = []

    to_time_zone: tzinfo = tz.gettz('Europe/Minsk')

    for message in messages:

        date_time_iso: Any = message.date.isoformat()
        date_time_obj: Any = dateutil.parser.isoparse(date_time_iso)
        date_time_obj: Any = date_time_obj.astimezone(to_time_zone)

        result_date: str = date_time_obj.strftime('%m-%d-%Y %H:%M:%S')

        if message.message:

            result_list.append({'message': message.message.replace('\n', ' '),
                                'datetime': result_date,
                                'from_admin': message.post_author})

        else:

            result_list.append({'message': '<image>',
                                'datetime': result_date,
                                'from_admin': message.post_author})

    channel_title: str = re.sub(r'[^a-zA-Zа-яА-Я0-9]', '_', channel.title)

    with open(f'content/{channel_title}.json', 'w', encoding='utf8') as file:

        json.dump({channel_title: result_list}, file, indent=4, ensure_ascii=False)

    return channel_title
