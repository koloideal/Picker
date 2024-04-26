from aiogram import types
from get_data_telegram.get_messages_from_group import get_messages_from_group
from aiogram.types import FSInputFile
import os


async def action_00_for_callback(callback: types.CallbackQuery, action: str) -> None:

    link, limit = action.split()

    processed = await callback.message.answer('Processed...')

    file_name: str = await get_messages_from_group(link, limit)

    await processed.delete()

    full_file_name: str = f'messages_of_groups_to_json/{file_name}.json'

    document: FSInputFile = FSInputFile(full_file_name)

    await callback.message.answer_document(document=document)

    os.remove(full_file_name)

    return None
