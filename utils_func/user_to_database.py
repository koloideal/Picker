import datetime
import sqlite3
from aiogram import types


async def user_to_database(message: types.Message) -> None:

    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_username = message.from_user.username

    try:

        connection = sqlite3.connect('../database/bot_users.db')
        cursor = connection.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                          (id int, first_name varchar(50), username varchar(50))''')
        connection.commit()

        cursor.execute('''SELECT id FROM users''')
        id_from_bot_users = cursor.fetchall()
        connection.commit()

        cursor.close()
        connection.close()

        id_from_bot_users = [x[0] for x in id_from_bot_users]

        for us_id in id_from_bot_users:

            if user_id == us_id:

                return

            else:

                continue

        connection = sqlite3.connect('../database/bot_users.db')
        cursor = connection.cursor()

        cursor.execute('''INSERT INTO users (id, first_name, username)
                           VALUES (?, ?, ?)''',
                           (user_id, user_first_name, user_username))
        connection.commit()

        cursor.close()
        connection.close()

        with open('../secret_data/logs.txt', 'a', encoding='utf8') as logs:

            logs.write(f'Дата {datetime.datetime.now()}\nЮзер @{user_username} добавлен в базу данных\n\n')

    except Exception as e:

        with open('../secret_data/errors.txt', 'w') as errors:

            errors.write(f'Дата {datetime.datetime.now()}\nОшибка {e}\n\n')
