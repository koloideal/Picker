from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def button_to_help_rout(message: Message) -> None:

    get_inf_but: InlineKeyboardButton = InlineKeyboardButton(text='Information about command /search',
                                                             callback_data='get_inf_but')

    get_big_inf: InlineKeyboardButton = InlineKeyboardButton(text='Privacy Information',
                                                             callback_data='get_big_inf')

    get_tech_inf: InlineKeyboardButton = InlineKeyboardButton(text='Technical information',
                                                              callback_data='get_tech_inf')

    buttons: list = [

        [get_inf_but],
        [get_big_inf],
        [get_tech_inf]
    ]

    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=buttons)

    await message.answer('<b>Select the necessary button</b>', reply_markup=keyboard)

    return
