from aiogram import types
import os
from handlers.router_func.rout_start import creator_id


async def drop_data_rout(message: types.Message) -> None:

    user_id: int = message.from_user.id

    if user_id != creator_id:

        await message.answer('Unknown command, enter /help')

    else:

        try:

            os.remove('database/admin_users.db')
            os.remove('database/bot_users.db')
            os.remove('database/banned_users.db')

            with open('secret_data/logs.txt', 'w'):
                pass

        except FileNotFoundError:
            pass

        finally:

            await message.answer('<i>I hope everything is fine</i>')

    return
