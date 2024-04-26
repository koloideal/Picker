from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def get_url_for_posts_in_channel_rout(message: types.Message, state: FSMContext):

    if message.text.startswith('t.me') or message.text.startswith('https://t.me'):

        builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

        builder.row(InlineKeyboardButton(text='20', callback_data=f'{message.text} 20p'),
                    InlineKeyboardButton(text='100', callback_data=f'{message.text} 100p'),
                    InlineKeyboardButton(text='500', callback_data=f'{message.text} 500p'),
                    InlineKeyboardButton(text='1k', callback_data=f'{message.text} 1000p'),
                    InlineKeyboardButton(text='3k', callback_data=f'{message.text} 3000p'))

        await message.answer('<b>Выберите количество собираемых сообщений</b>', reply_markup=builder.as_markup())

    else:

        await message.answer('This is not link')

        await state.clear()
