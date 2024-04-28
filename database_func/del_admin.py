import sqlite3
from sqlite3 import Connection, Cursor
from aiogram import types
import logging


async def del_admin(message: types.Message, ex_admin: dict) -> None:

    ex_admin_id = ex_admin["user_id"]
    ex_admin_username = ex_admin["user_username"]

    connection: Connection = sqlite3.connect('database/admin_users.db')
    cursor: Cursor = connection.cursor()

    cursor.execute('''DELETE FROM admin_users WHERE id = ?''', (ex_admin_id,))

    connection.commit()

    cursor.close()
    connection.close()

    logging.warning(f'Юзер @{ex_admin_username} теперь не админ')

    await message.answer(f'@{ex_admin_username} теперь не админ')
