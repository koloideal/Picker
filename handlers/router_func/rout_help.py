from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def button_to_help_rout(message: Message):

    get_inf_but: InlineKeyboardButton = InlineKeyboardButton(text='Информация о кнопках команды /search',
                                                             callback_data='get_inf_but')

    get_big_inf: InlineKeyboardButton = InlineKeyboardButton(text='Информация о конфиденциальности',
                                                             callback_data='get_big_inf')

    get_tech_inf: InlineKeyboardButton = InlineKeyboardButton(text='Техническая информация',
                                                              callback_data='get_tech_inf')

    get_all_inf: InlineKeyboardButton = InlineKeyboardButton(text='Вся информация',
                                                             callback_data='get_all_inf')

    buttons: list = [

        [get_inf_but],
        [get_big_inf],
        [get_tech_inf],
        [get_all_inf]
    ]

    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=buttons)

    await message.answer('<b>Выберите кнопку с интересующей информацией</b>', reply_markup=keyboard)
