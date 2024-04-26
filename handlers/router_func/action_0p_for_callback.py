from aiogram import types
from get_data_telegram.get_posts_from_channel import get_posts_from_channel
from aiogram.types import FSInputFile
import os


async def action_0p_for_callback(callback: types.CallbackQuery, action: str) -> None:

    link, limit = action.split()

    processed = await callback.message.answer('Processed...')

    file_name: str = await get_posts_from_channel(link, limit[:-1])

    full_file_name: str = f'posts_of_channel_to_json/{file_name}.json'

    document: FSInputFile = FSInputFile(full_file_name)

    await callback.message.answer_document(document=document)

    await processed.delete()

    os.remove(full_file_name)

    return None
