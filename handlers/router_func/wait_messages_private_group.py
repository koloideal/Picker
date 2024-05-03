from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


class CallbackForGetMessagesInPrivate(CallbackData, prefix="my", sep="#"):

    action: str
    link: str
    limit: int


async def get_url_for_messages_in_private_group_rout(message: types.Message, state: FSMContext):

    limit_100 = CallbackForGetMessagesInPrivate(action='get_messages_private', link=message.text, limit=100).pack()
    limit_500 = CallbackForGetMessagesInPrivate(action='get_messages_private', link=message.text, limit=500).pack()
    limit_2k = CallbackForGetMessagesInPrivate(action='get_messages_private', link=message.text, limit=2000).pack()
    limit_5k = CallbackForGetMessagesInPrivate(action='get_messages_private', link=message.text, limit=5000).pack()
    limit_10k = CallbackForGetMessagesInPrivate(action='get_messages_private', link=message.text, limit=10000).pack()

    if message.text.startswith('t.me/+') or message.text.startswith('https://t.me/+'):

        builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

        builder.row(InlineKeyboardButton(text='100', callback_data=limit_100),
                    InlineKeyboardButton(text='500', callback_data=limit_500),
                    InlineKeyboardButton(text='2k', callback_data=limit_2k),
                    InlineKeyboardButton(text='5k', callback_data=limit_5k),
                    InlineKeyboardButton(text='10k', callback_data=limit_10k))

        await message.answer('<b>Выберите количество собираемых сообщений</b>', reply_markup=builder.as_markup())

    else:

        await message.answer('This is not link')

        await state.clear()
