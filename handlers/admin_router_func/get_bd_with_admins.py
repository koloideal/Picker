from aiogram import types
from utils_func.get_admins import get_admins
from aiogram.types import FSInputFile
from datetime import datetime
import sqlite3
from sqlite3 import Connection, Cursor
import json
import os


async def get_admin_bd_rout(message: types.Message):

    user_id = message.from_user.id

    admins_id = await get_admins()

    if user_id != 2047958833 and user_id not in admins_id:

        await message.answer('Unknown command\n'
                             'Enter /help to get help')

    else:

        connection: Connection = sqlite3.connect('database/admin_users.db')
        cursor: Cursor = connection.cursor()

        cursor.execute('''SELECT * FROM admin_users''')

        all_admins = cursor.fetchall()

        cursor.close()
        connection.close()

        if not all_admins:

            await message.answer('Database is empty, add an admin and try again')

            return

        to_dump_data = {}

        for admin in all_admins:

            to_dump_data[admin[3]] = {

                'admin_id': admin[0],
                'admin_first_name': admin[1],
                'admin_last_name': admin[2],
                'admin_username': admin[3]

            }

        full_file_name: str = f'secret_data/admin_users.json'

        with open(full_file_name, 'w', encoding='utf8') as file:

            json.dump(to_dump_data, file, indent=4, ensure_ascii=False)

        document: FSInputFile = FSInputFile(full_file_name)

        await message.answer_document(document=document, caption=f'before {datetime.now().strftime('%d-%m-%Y')}')

        os.remove(full_file_name)
