import sqlite3
from sqlite3 import Connection, Cursor
from aiogram import types
import logging


async def user_to_database(message: types.Message) -> None:

    user_id: int = message.from_user.id
    user_first_name: str = message.from_user.first_name
    user_username: str = message.from_user.username

    connection: Connection = sqlite3.connect('database/bot_users.db')
    cursor: Cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                              (id int,
                               first_name varchar(50),
                               username varchar(50),
                               UNIQUE(id))''')
    connection.commit()

    cursor.execute('''INSERT OR IGNORE INTO users (id, first_name, username)
                      VALUES (?, ?, ?)''',
                   (user_id, user_first_name, user_username))

    connection.commit()

    cursor.close()
    connection.close()

    logging.warning(f'Юзер @{user_username} добавлен в базу данных или уже существует в ней')
