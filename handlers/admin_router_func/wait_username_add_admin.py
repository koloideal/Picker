from aiogram import types
from aiogram.fsm.context import FSMContext
from configparser import ConfigParser
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import UsernameInvalidError
from utils_func.admin_to_database import admin_to_database


config: ConfigParser = ConfigParser()
config.read("secret_data/config.ini")


api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']


client = TelegramClient('session', int(api_id), api_hash)


async def get_username_for_add_admin_rout(message: types.Message, state: FSMContext):

    try:

        await client.connect()

        if message.text.startswith('t.me/') or message.text.startswith('https://t.me/'):

            raise ValueError

        future_admin_username = message.text if message.text[0] != '@' else message.text[1:]

        user = await client.get_participants(future_admin_username)

        if user[0].bot or len(user) != 1:

            raise ValueError

    except (UsernameInvalidError, ValueError) as e:

        await message.answer('Некорректный юзернейм')

    else:

        user_username = future_admin_username
        user_id = user[0].id
        user_first_name = user[0].first_name
        user_last_name = user[0].last_name

        await admin_to_database(message=message, future_admin={

            'user_id': user_id,
            'user_first_name': user_first_name,
            'user_last_name': user_last_name,
            'user_username': user_username

        })

    finally:

        await client.disconnect()

        await state.clear()
