from aiogram import types
import os


async def drop_data_rout(message: types.Message):

    user_id = message.from_user.id

    if user_id != 2047958833:

        await message.answer('Unknown command\n'
                             'Enter /help to get help')

    else:

        try:

            os.remove('database/admin_users.db')
            os.remove('database/bot_users.db')

            with open('secret_data/logs.txt', 'w'):
                pass

        except FileNotFoundError:

            pass

        finally:

            await message.answer('<i>I hope everything is fine</i>')
