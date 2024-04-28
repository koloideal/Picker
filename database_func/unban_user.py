import sqlite3
from sqlite3 import Connection, Cursor
from aiogram import types
import logging
from database_func.get_banned_users import get_banned_users


async def unban_user(message: types.Message, ex_ban_user: dict) -> None:

    banned_users = await get_banned_users()

    user_username = ex_ban_user['user_username']
    user_id = ex_ban_user['user_id']

    if user_id not in banned_users:

        await message.answer(f'Юзер @{user_username} не был забанен')

    else:

        connection: Connection = sqlite3.connect('database/banned_users.db')
        cursor: Cursor = connection.cursor()

        cursor.execute('''DELETE FROM banned_users WHERE id = ?''', (user_id,))

        connection.commit()

        cursor.close()
        connection.close()

        logging.warning(f'Юзер @{user_username} разбанен')

        await message.answer(f'@{user_username} разбанен')
