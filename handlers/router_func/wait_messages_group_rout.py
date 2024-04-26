from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def get_url_for_messages_in_group_rout(message: types.Message, state: FSMContext):
    if message.text.startswith('t.me') or message.text.startswith('https://t.me'):

        builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

        builder.row(InlineKeyboardButton(text='100', callback_data=f'{message.text} 100'),
                    InlineKeyboardButton(text='500', callback_data=f'{message.text} 500'),
                    InlineKeyboardButton(text='2k', callback_data=f'{message.text} 2000'),
                    InlineKeyboardButton(text='5k', callback_data=f'{message.text} 5000'),
                    InlineKeyboardButton(text='10k', callback_data=f'{message.text} 10000'))

        await message.answer('<b>Выберите количество собираемых сообщений</b>', reply_markup=builder.as_markup())

    else:

        await message.answer('This is not link')

        await state.clear()
