from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.state import StatesGroup, State
from database_func.get_banned_users import get_banned_users


class SearchState(StatesGroup):
    waiting_for_get_participants_from_channel: State = State()
    waiting_for_get_participants_from_group: State = State()
    waiting_for_get_messages_from_group: State = State()
    waiting_for_get_posts_from_channel: State = State()
    waiting_for_get_users_from_private_group: State = State()
    waiting_for_get_messages_from_private_group: State = State()


class AdminState(StatesGroup):
    waiting_for_add_admin: State = State()
    waiting_for_del_admin: State = State()
    waiting_for_ban_user: State = State()
    waiting_for_unban_user: State = State()


async def button_to_search_rout(message: Message) -> None:

    user_id: int = message.from_user.id

    banned_users: list = await get_banned_users()

    if (user_id in banned_users) and (user_id != 2047958833):

        await message.answer(f"You can't use the bot."
                             f"\n\n<u><b>You were blocked</b></u>"
                             f"\n\n\nAbout the unban - <a href='https://t.me/kolo_id'>kolo</a>",
                             disable_web_page_preview=True)

    else:

        get_us_groups: InlineKeyboardButton = InlineKeyboardButton(text='1. Get Users From Groups',
                                                                   callback_data='get_us_groups')

        get_us_channel: InlineKeyboardButton = InlineKeyboardButton(text='2. Get Users From Channel',
                                                                    callback_data='get_us_channel')

        get_mes_groups: InlineKeyboardButton = InlineKeyboardButton(text='3. Get Messages From Groups',
                                                                    callback_data='get_mes_groups')

        get_pos_channel: InlineKeyboardButton = InlineKeyboardButton(text='4. Get Posts From Channel',
                                                                     callback_data='get_pos_channel')

        get_us_private_groups: InlineKeyboardButton = InlineKeyboardButton(text='5. Get Users From Private Groups',
                                                                           callback_data='get_us_private_groups')

        get_mes_private_groups: InlineKeyboardButton = InlineKeyboardButton(text='6. Get Message From Private Groups',
                                                                            callback_data='get_mes_private_groups')

        buttons: list = [

            [get_us_groups],
            [get_us_channel],
            [get_mes_groups],
            [get_pos_channel],
            [get_us_private_groups],
            [get_mes_private_groups]

        ]

        keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=buttons)

        await message.answer('<b>Select the necessary button to search</b>', reply_markup=keyboard)

    return
