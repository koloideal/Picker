from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


class CallbackForGetPosts(CallbackData, prefix="my", sep="#"):

    action: str
    link: str
    limit: int


async def get_url_for_posts_in_channel_rout(message: types.Message, state: FSMContext):

    limit_20 = CallbackForGetPosts(action='get_posts', link=message.text, limit=20).pack()
    limit_100 = CallbackForGetPosts(action='get_posts', link=message.text, limit=100).pack()
    limit_500 = CallbackForGetPosts(action='get_posts', link=message.text, limit=500).pack()
    limit_1k = CallbackForGetPosts(action='get_posts', link=message.text, limit=1000).pack()
    limit_3k = CallbackForGetPosts(action='get_posts', link=message.text, limit=3000).pack()

    if message.text.startswith('t.me') or message.text.startswith('https://t.me'):

        builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

        builder.row(InlineKeyboardButton(text='20', callback_data=limit_20),
                    InlineKeyboardButton(text='100', callback_data=limit_100),
                    InlineKeyboardButton(text='500', callback_data=limit_500),
                    InlineKeyboardButton(text='1k', callback_data=limit_1k),
                    InlineKeyboardButton(text='3k', callback_data=limit_3k))

        await message.answer('<b>Выберите количество собираемых сообщений</b>', reply_markup=builder.as_markup())

    else:

        await message.answer('This is not link')

        await state.clear()
