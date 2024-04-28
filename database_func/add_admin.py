import sqlite3
from sqlite3 import Connection, Cursor
from aiogram import types
import logging


async def admin_to_database(message: types.Message, future_admin: dict) -> None:

    user_username = future_admin['user_username']
    user_id = future_admin['user_id']
    user_first_name = future_admin['user_first_name']
    user_last_name = future_admin['user_last_name']

    connection: Connection = sqlite3.connect('database/admin_users.db')
    cursor: Cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS admin_users 
                      (id int,
                      first_name varchar(50),
                      last_name varchar(50),
                      username varchar(50),
                      UNIQUE(id))''')

    connection.commit()

    cursor.execute('''INSERT OR IGNORE INTO admin_users (id, first_name, last_name, username)
                      VALUES (?, ?, ?, ?)''',
                   (user_id, user_first_name, user_last_name, user_username))

    connection.commit()

    cursor.close()
    connection.close()

    logging.warning(f'Юзер @{user_username} теперь админ или уже им был')

    await message.answer(f'@{user_username} теперь админ или уже был им')
