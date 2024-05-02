from aiogram import types
from get_data_telegram.get_messages_from_group import get_messages_from_group
from aiogram.types import FSInputFile
import os
from handlers.router_func.wait_messages_group_rout import CallbackForGetMessages
from aiogram.fsm.context import FSMContext
import logging


async def second_step_to_get_messages(callback: types.CallbackQuery,
                                      callback_data: CallbackForGetMessages,
                                      state: FSMContext) -> None:
    try:

        await callback.message.delete()

        link = callback_data.link
        limit = callback_data.limit

        processed = await callback.message.answer('Processed...')

        file_name: str = await get_messages_from_group(link, limit)

    except Exception as e:

        logging.error(e)

        await callback.message.answer('Некорректная ссылка')

    else:

        full_file_name: str = f'messages_of_groups_to_json/{file_name}.json'

        document: FSInputFile = FSInputFile(full_file_name)

        await callback.message.answer_document(document=document)

        await processed.delete()

        os.remove(full_file_name)

    finally:

        await state.clear()

        return None
