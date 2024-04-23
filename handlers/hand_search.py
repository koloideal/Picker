from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.state import StatesGroup, State


class SearchState(StatesGroup):

    waiting_for_search_participants_of_channel: State = State()
    waiting_for_search_participants_of_group: State = State()


async def search(message: Message) -> None:

    get_us_groups: InlineKeyboardButton = InlineKeyboardButton(text='Get Users From Groups',
                                                               callback_data='get_us_groups')

    get_us_channel: InlineKeyboardButton = InlineKeyboardButton(text='Get Users From Channel',
                                                                callback_data='get_us_channel')

    get_mes_groups: InlineKeyboardButton = InlineKeyboardButton(text='Get Messages From Groups',
                                                                callback_data='get_mes_groups')

    get_mes_channel: InlineKeyboardButton = InlineKeyboardButton(text='Get Messages From Channel',
                                                                 callback_data='get_mes_channel')

    buttons: list = [

        [get_us_groups],
        [get_us_channel],
        [get_mes_groups],
        [get_mes_channel]

    ]

    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=buttons)

    await message.answer('<b>Выберите кнопку исходя из вашего запроса</b>', reply_markup=keyboard)

