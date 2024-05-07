import sqlite3
from sqlite3 import Connection, Cursor
from aiogram import types
import logging
from database_func.get_banned_users import get_banned_users


async def unban_user(message: types.Message, ex_ban_user: dict) -> None:

    banned_users: list = await get_banned_users()

    user_username: str = ex_ban_user['user_username']
    user_id: int = ex_ban_user['user_id']

    if user_id not in banned_users:

        await message.answer(f'User @{user_username} was not banned')

    else:

        connection: Connection = sqlite3.connect('database/banned_users.db')
        cursor: Cursor = connection.cursor()

        cursor.execute('''DELETE FROM banned_users WHERE id = ?''', (user_id,))

        connection.commit()

        cursor.close()
        connection.close()

        logging.warning(f'User @{user_username} unbanned')

        await message.answer(f'@{user_username} unbanned')
