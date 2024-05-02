from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from get_data_telegram.get_users_from_private_group import get_users_from_private_groups
import os


async def get_url_for_users_in_private_groups_rout(message: types.Message, state: FSMContext):

    if message.text.startswith('t.me/+') or message.text.startswith('https://t.me/+'):

        processed = await message.answer('Processed...')

        file_name: str = await get_users_from_private_groups(message)

        if not file_name:

            await processed.delete()

            await state.clear()

        else:

            full_file_name: str = f'users_of_private_groups_to_json/{file_name}.json'

            document: FSInputFile = FSInputFile(full_file_name)

            await message.answer_document(document=document)

            await processed.delete()

            os.remove(full_file_name)

            await state.clear()

    else:

        await message.answer('This is not link')

        await state.clear()
