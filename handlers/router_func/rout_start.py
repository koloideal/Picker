from aiogram import types
from database_func.user_to_database import user_to_database
from database_func.get_admins import get_admins
from database_func.get_banned_users import get_banned_users
from configparser import ConfigParser


config = ConfigParser()
config.read('secret_data/config.ini')

creator_id: int = int(config['Telegram']['creator_id'])


async def start_rout(message: types.Message) -> None:

    user_id: int = message.from_user.id

    admins_id: list = await get_admins()

    banned_users_id: list = await get_banned_users()

    case1: bool = user_id in admins_id and user_id == creator_id
    case2: bool = user_id not in admins_id and user_id == creator_id
    case3: bool = user_id in admins_id and user_id != creator_id
    case4: bool = user_id in banned_users_id
    case5: bool = user_id not in banned_users_id

    creator_case: bool = ((case1 and case5) or (case2 and case5)) and not case4
    admin_case: bool = case3 and case5 and not (case4 or case1 or case2)
    user_case: bool = case5 and not (case1 or case2 or case3 or case4)
    banned_user_case: bool = (case4 and not (case1 or case2 or case3 or case5)) or (case4 and case3)

    if creator_case:

        await message.answer(f"Hello, Creator\n\n"
                             f"What do you want to do today? 💭"
                             f"\n\nFor reference, click <b><i>/help</i></b> 👈\n\n"
                             f"To get started, click <b><i>/search</i></b>👈\n\n"
                             f"---------- Creator's Commands👇----------\n\n"
                             f"Add admin - <b><i>/add_admin</i></b> 👈\n\n"
                             f"Delete admin - <b><i>/del_admin</i></b> 👈\n\n"
                             f"Ban the user - <b><i>/ban_user</i></b> 👈\n\n"
                             f"Unban the user - <b><i>/unban_user</i></b> 👈\n\n"
                             f"Get logs - <b><i>/get_logs</i></b> 👈\n\n"
                             f"json with users - <b><i>/get_users_bd</i></b> 👈\n\n"
                             f"json with admins - <b><i>/get_admins_bd</i></b> 👈\n\n"
                             f"json with ban users - <b><i>/get_ban_users_bd</i></b>\n\n"
                             f"<strike>You know the rest</strike>"
                             f"\n\n\n<b><i>made by you 🫵</i></b>")

    elif admin_case:

        await message.answer(f"Hello, admin\n\n"
                             f"What do you want to do today? 💭"
                             f"\n\nfor help, click <b><i>/help</i></b> 👈\n\n"
                             f"To get started, press <b><i>/search</i></b> 👈\n\n"
                             f"---------- Admin Commands👇----------\n\n"
                             f"Ban the user - <b><i>/ban_user</i></b> 👈\n\n"
                             f"Unban the user - <b><i>/unban_user</i></b> 👈\n\n"
                             f"Get logs - <b><i>/get_logs</i></b> 👈\n\n"
                             f"json with users - <b><i>/get_users_bd</i></b> 👈\n\n"
                             f"json with admins - <b><i>/get_admins_bd</i></b> 👈\n\n"
                             f"json with ban users - <b><i>/get_ban_users_bd</i></b>"
                             f"\n\n\n<b><i>made by <a href='https://t.me/kolo_id '>kolo</a></i></b>",
                             disable_web_page_preview=True)

    elif user_case:

        await message.answer(f"Hello, I am a <b>Picker</b>🤖\n\nBot for collecting information"
                             f" from chats and channels in <b><i>Telegram</i></b> 💭"
                             f"\n\nFor help, click <b><i>/help</i></b> 👈\n\n"
                             f"To get started, press <b><i>/search</i></b>👈"
                             f"\n\n\n<b><i>made by <a href='https://t.me/kolo_id'>kolo</a></i></b>",
                             disable_web_page_preview=True)

    elif banned_user_case:

        await message.answer(f"Hello, I am a <b>Picker</b>🤖\n\nBot for collecting information"
                             f" from chats and channels in <b><i>Telegram</i></b> 💭"
                             f"\n\n<u><b>You were blocked</b></u>"
                             f"\n\n\nAbout the unban - <a href='https://t.me/kolo_id'>kolo</a>",
                             disable_web_page_preview=True)

    await user_to_database(message)

    return
