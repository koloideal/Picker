from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.state import StatesGroup, State


class SearchState(StatesGroup):

    waiting_for_get_participants_of_channel: State = State()
    waiting_for_get_participants_of_group: State = State()
    waiting_for_get_messages_of_group: State = State()
    waiting_for_get_posts_of_channel: State = State()


class AdminState(StatesGroup):

    waiting_for_add_admin: State = State()
    waiting_for_del_admin: State = State()


async def button_to_search_rout(message: Message) -> None:

    get_us_groups: InlineKeyboardButton = InlineKeyboardButton(text='Get Users From Groups',
                                                               callback_data='get_us_groups')

    get_us_channel: InlineKeyboardButton = InlineKeyboardButton(text='Get Users From Channel',
                                                                callback_data='get_us_channel')

    get_mes_groups: InlineKeyboardButton = InlineKeyboardButton(text='Get Messages From Groups',
                                                                callback_data='get_mes_groups')

    get_pos_channel: InlineKeyboardButton = InlineKeyboardButton(text='Get Posts From Channel',
                                                                 callback_data='get_pos_channel')

    buttons: list = [

        [get_us_groups],
        [get_us_channel],
        [get_mes_groups],
        [get_pos_channel]

    ]

    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=buttons)

    await message.answer('<b>Выберите кнопку исходя из вашего запроса</b>', reply_markup=keyboard)


