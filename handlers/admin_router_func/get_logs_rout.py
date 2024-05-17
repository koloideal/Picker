from aiogram import types
from database_func.get_admins import get_admins
from aiogram.types import FSInputFile
from datetime import datetime
from aiogram.exceptions import TelegramBadRequest
from handlers.router_func.rout_start import creator_id


async def get_logs_rout(message: types.Message) -> None:

    user_id: int = message.from_user.id

    admins_id: list = await get_admins()

    if user_id != creator_id and user_id not in admins_id:

        await message.answer('Unknown command, enter /help')

    else:

        full_file_name: str = f'secret_data/logs.txt'

        document: FSInputFile = FSInputFile(full_file_name)

        captions: str = f'before {datetime.now().strftime('%d-%m-%Y')}'

        try:

            await message.answer_document(document=document, caption=captions)

        except TelegramBadRequest:

            await message.answer('Logs are empty, enter /start and try again')

    return
