from aiogram import types
from aiogram.fsm.context import FSMContext
from configparser import ConfigParser
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import UsernameInvalidError
from database_func.unban_user import unban_user


config: ConfigParser = ConfigParser()
config.read("secret_data/config.ini")


api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']


client = TelegramClient('session', int(api_id), api_hash)


async def get_username_for_unban_user_rout(message: types.Message, state: FSMContext):

    try:

        await client.start()

        if message.text.startswith('t.me/') or message.text.startswith('https://t.me/'):

            raise ValueError

        ex_ban_user_username = message.text if message.text[0] != '@' else message.text[1:]

        user = await client.get_participants(ex_ban_user_username)

        user_id = user[0].id
        user_username = user[0].username
        user_first_name = user[0].first_name
        user_last_name = user[0].last_name

        if len(user) != 1:

            raise ValueError

    except (UsernameInvalidError, ValueError):

        await message.answer('Некорректный юзернейм')

    else:

        await unban_user(message=message, ex_ban_user={

            'user_id': user_id,
            'user_first_name': user_first_name,
            'user_last_name': user_last_name,
            'user_username': user_username

        })

    finally:

        await client.disconnect()

        await state.clear()
