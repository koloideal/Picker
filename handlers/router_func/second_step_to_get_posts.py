import logging
from aiogram.fsm.context import FSMContext
from aiogram import types
from get_data_telegram.get_posts_from_channel import get_posts_from_channel
from aiogram.types import FSInputFile
import os
from handlers.router_func.wait_posts_channel_rout import CallbackForGetPosts
from aiogram.types.message import Message


async def second_step_to_get_posts(callback: types.CallbackQuery,
                                   callback_data: CallbackForGetPosts,
                                   state: FSMContext) -> None:

    try:

        await callback.message.delete()

        link: str = callback_data.link
        limit: int = callback_data.limit

        processed: Message = await callback.message.answer('Processed...')

        file_name: str = await get_posts_from_channel(link, limit)

    except Exception as e:

        logging.error(e)

        await callback.message.answer('Invalid link')

    else:

        full_file_name: str = f'content/{file_name}.json'

        document: FSInputFile = FSInputFile(full_file_name)

        await callback.message.answer_document(document=document)

        await processed.delete()

        os.remove(full_file_name)

    finally:

        await state.clear()

        return
