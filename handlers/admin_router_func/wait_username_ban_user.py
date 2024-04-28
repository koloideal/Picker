from aiogram import types
from aiogram.fsm.context import FSMContext
from configparser import ConfigParser
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import UsernameInvalidError
from database_func.ban_user import ban_user
from database_func.get_admins import get_admins
from database_func.del_admin import del_admin


config: ConfigParser = ConfigParser()
config.read("secret_data/config.ini")


api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']


client = TelegramClient('session', int(api_id), api_hash)


async def get_username_for_ban_user_rout(message: types.Message, state: FSMContext):

    try:

        await client.start()

        if message.text.startswith('t.me/') or message.text.startswith('https://t.me/'):

            raise ValueError

        future_ban_user_username = message.text if message.text[0] != '@' else message.text[1:]

        user = await client.get_participants(future_ban_user_username)

        user_id = user[0].id
        user_username = user[0].username
        user_first_name = user[0].first_name
        user_last_name = user[0].last_name

        admins_id = await get_admins()

        if ((user_id in admins_id) or (user_id == 2047958833)) and message.from_user.id != 2047958833:

            raise TypeError

        if len(user) != 1:

            raise ValueError

    except (UsernameInvalidError, ValueError):

        await message.answer('Некорректный юзернейм')

    except TypeError:

        await message.answer('Ты не можешь забанить админа или Создателя')

    else:

        if user_id in admins_id:

            await del_admin(message=message, ex_admin={

                'user_id': user_id,
                'user_username': user_username

            })

        await ban_user(message=message, future_ban_user={

            'user_id': user_id,
            'user_first_name': user_first_name,
            'user_last_name': user_last_name,
            'user_username': user_username

        })

    finally:

        await client.disconnect()

        await state.clear()
