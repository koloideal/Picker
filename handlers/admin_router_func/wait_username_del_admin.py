from aiogram import types
from aiogram.fsm.context import FSMContext
from configparser import ConfigParser
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import UsernameInvalidError
from database_func.del_admin import del_admin
from database_func.get_admins import get_admins


config: ConfigParser = ConfigParser()
config.read("secret_data/config.ini")


api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']


client = TelegramClient('session', int(api_id), api_hash)


async def get_username_for_del_admin_rout(message: types.Message, state: FSMContext):

    try:

        admin_id = await get_admins()

        await client.start()

        if message.text.startswith('t.me/') or message.text.startswith('https://t.me/'):

            raise ValueError

        ex_admin_username = message.text if message.text[0] != '@' else message.text[1:]

        user = await client.get_participants(ex_admin_username)

        user_id = user[0].id
        user_username = user[0].username

        if len(user) != 1:

            raise ValueError

        if user_id not in admin_id:

            raise TypeError

    except (UsernameInvalidError, ValueError):

        await message.answer('Некорректный юзернейм')

    except TypeError:

        await message.answer('Человек не является админом')

    else:

        await del_admin(message=message, ex_admin={

            'user_id': user_id,
            'user_username': user_username

        })

    finally:

        await client.disconnect()

        await state.clear()
