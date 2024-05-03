from aiogram import types
from get_data_telegram.get_messages_from_private_group import get_messages_from_private_group
from aiogram.types import FSInputFile
import os
from handlers.router_func.wait_messages_private_group import CallbackForGetMessagesInPrivate
from aiogram.fsm.context import FSMContext
import logging


async def second_step_to_get_messages_private(callback: types.CallbackQuery,
                                              callback_data: CallbackForGetMessagesInPrivate,
                                              state: FSMContext) -> None:
    try:

        await callback.message.delete()

        link = callback_data.link
        limit = callback_data.limit

        processed = await callback.message.answer('Processed...')

        file_name: str = await get_messages_from_private_group(link, limit)

    except Exception as e:

        print(e)

        logging.error(e)

        await callback.message.answer('Некорректная ссылка')

    else:

        if file_name:

            full_file_name: str = f'messages_of_private_groups_to_json/{file_name}.json'

            document: FSInputFile = FSInputFile(full_file_name)

            await callback.message.answer_document(document=document)

            os.remove(full_file_name)

        else:

            await callback.message.answer('Слишком много попыток, попробуйте через 10 минут')

    finally:

        await processed.delete()

        await state.clear()

        return None
