from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from get_data_telegram.get_users_from_channel import get_users_from_channel
import os


async def get_url_for_users_in_channel_rout(message: types.Message, state: FSMContext):

    if message.text.startswith('t.me') or message.text.startswith('https://t.me'):

        processed = await message.answer('Processed...')

        file_name: str = await get_users_from_channel(message.text)

        if file_name == '!ChatAdminRequiredError':

            await processed.delete()

            await message.answer('Вы должны быть владельцем или админом данного канала')

            await state.clear()

        elif file_name == '!ValueError':

            await processed.delete()

            await message.answer('Некорректная ссылка')

            await state.clear()

        else:

            await processed.delete()

            full_file_name: str = f'users_of_channels_to_json/{file_name}.json'

            document: FSInputFile = FSInputFile(full_file_name)

            await message.answer_document(document=document)

            os.remove(full_file_name)

            await state.clear()

    else:

        await message.answer('This is not link')

        await state.clear()
