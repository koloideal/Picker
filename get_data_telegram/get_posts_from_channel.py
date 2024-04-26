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


async def get_posts_from_channel(url, limit):

    await client.start()

    channel = await client.get_entity(url)

    messages = await client.get_messages(channel, limit=int(limit))

    result_list = []

    to_time_zone = tz.gettz('Europe/Minsk')

    for message in messages:

        date_time_iso = message.date.isoformat()
        date_time_obj = dateutil.parser.isoparse(date_time_iso)
        date_time_obj = date_time_obj.astimezone(to_time_zone)

        result_date = date_time_obj.strftime('%m-%d-%Y %H:%M:%S')

        if message.message:

            result_list.append({'message': message.message.replace('\n', ' '),
                                'datetime': result_date,
                                'from_admin': message.post_author})

        else:

            result_list.append({'message': '<image>',
                                'datetime': result_date,
                                'from_admin': message.post_author})

    channel_title = re.sub(r'[^a-zA-Zа-яА-Я0-9]', '_', channel.title)

    with open(f'posts_of_channel_to_json/{channel_title}.json', 'w', encoding='utf8') as file:

        json.dump({channel_title: result_list}, file, indent=4, ensure_ascii=False)

    return channel_title
