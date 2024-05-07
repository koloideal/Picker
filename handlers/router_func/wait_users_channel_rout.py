from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from get_data_telegram.get_users_from_channel import get_users_from_channel
import os
from aiogram.types.message import Message


async def get_url_for_users_in_channel_rout(message: Message, state: FSMContext) -> None:

    if message.text.startswith('t.me') or message.text.startswith('https://t.me'):

        processed: Message = await message.answer('Processed...')

        file_name: str = await get_users_from_channel(message)

        if not file_name:

            await processed.delete()

            await state.clear()

        else:

            full_file_name: str = f'content/{file_name}.json'

            document: FSInputFile = FSInputFile(full_file_name)

            await message.answer_document(document=document)

            await processed.delete()

            os.remove(full_file_name)

            await state.clear()

    else:

        await message.answer('This is not link')

        await state.clear()

    return
