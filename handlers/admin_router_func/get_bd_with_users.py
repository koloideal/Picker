from aiogram import types
from utils_func.get_admins import get_admins
from aiogram.types import FSInputFile
from datetime import datetime
import sqlite3
from sqlite3 import Connection, Cursor
import json
import os
from sqlite3 import OperationalError


async def get_users_bd_rout(message: types.Message):

    user_id = message.from_user.id

    admins_id = await get_admins()

    if user_id != 2047958833 and user_id not in admins_id:

        await message.answer('Unknown command\n'
                             'Enter /help to get help')

    else:

        try:

            connection: Connection = sqlite3.connect('database/bot_users.db')
            cursor: Cursor = connection.cursor()

            cursor.execute('''SELECT * FROM users''')

            all_users = cursor.fetchall()

        except OperationalError:

            await message.answer('Database is empty, enter /start and try again')

            cursor.close()
            connection.close()

            return

        else:

            cursor.close()
            connection.close()

        to_dump_data = {}

        for user in all_users:

            to_dump_data[user[2]] = {

                'user_id': user[0],
                'user_first_name': user[1],
                'user_username': user[2]

            }

        full_file_name: str = f'secret_data/bot_users.json'

        with open(full_file_name, 'w', encoding='utf8') as file:

            json.dump(to_dump_data, file, indent=4, ensure_ascii=False)

        document: FSInputFile = FSInputFile(full_file_name)

        await message.answer_document(document=document, caption=f'before {datetime.now().strftime('%d-%m-%Y')}')

        os.remove(full_file_name)