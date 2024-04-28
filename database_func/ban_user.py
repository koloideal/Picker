import sqlite3
from sqlite3 import Connection, Cursor
from aiogram import types
import logging


async def ban_user(message: types.Message, future_ban_user: dict) -> None:

    user_username = future_ban_user['user_username']
    user_id = future_ban_user['user_id']
    user_first_name = future_ban_user['user_first_name']
    user_last_name = future_ban_user['user_last_name']

    connection: Connection = sqlite3.connect('database/banned_users.db')
    cursor: Cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS banned_users 
                      (id int,
                      first_name varchar(50),
                      last_name varchar(50),
                      username varchar(50),
                      UNIQUE(id))''')

    connection.commit()

    cursor.execute('''INSERT OR IGNORE INTO banned_users (id, first_name, last_name, username)
                      VALUES (?, ?, ?, ?)''',
                   (user_id, user_first_name, user_last_name, user_username))

    connection.commit()

    cursor.close()
    connection.close()

    logging.warning(f'Юзер @{user_username} забанен или уже был забанен')

    await message.answer(f'@{user_username} забанен или уже был забанен')
