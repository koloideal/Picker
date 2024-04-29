from aiogram import types
from database_func.user_to_database import user_to_database
from database_func.get_admins import get_admins
from database_func.get_banned_users import get_banned_users


async def start_rout(message: types.Message) -> None:

    user_id: int = message.from_user.id

    admins_id: list = await get_admins()

    banned_users_id = await get_banned_users()

    case1 = user_id in admins_id and user_id == 2047958833
    case2 = user_id not in admins_id and user_id == 2047958833
    case3 = user_id in admins_id and user_id != 2047958833
    case4 = user_id in banned_users_id
    case5 = user_id not in banned_users_id

    creator_case = ((case1 and case5) or (case2 and case5)) and not case4
    admin_case = case3 and case5 and not (case4 or case1 or case2)
    user_case = case5 and not (case1 or case2 or case3 or case4)
    banned_user_case = (case4 and not (case1 or case2 or case3 or case5)) or (case4 and case3)

    if creator_case:

        await message.answer(f"Здравствуй, Создатель\n\n"
                             f"Что хочешь сделать сегодня? 💭"
                             f"\n\nДля справки нажмите <b><i>/help</i></b> 👈\n\n"
                             f"Для начала работы нажмите <b><i>/search</i></b>👈\n\n"
                             f"----------Команды создателя👇----------\n\n"
                             f"Добавить админа - <b><i>/add_admin</i></b> 👈\n\n"
                             f"Удалить админа - <b><i>/del_admin</i></b> 👈\n\n"
                             f"Забанить юзера - <b><i>/ban_user</i></b> 👈\n\n"
                             f"Разбанить юзера - <b><i>/unban_user</i></b> 👈\n\n"
                             f"Получить логи - <b><i>/get_logs</i></b> 👈\n\n"
                             f"json с юзерами - <b><i>/get_users_bd</i></b> 👈\n\n"
                             f"json с админами - <b><i>/get_admins_bd</i></b> 👈\n\n"
                             f"json с ban-юзерами - <b><i>/get_ban_users_bd</i></b>\n\n"
                             f"<strike>You know the rest</strike>"
                             f"\n\n\n<b><i>made by you 🫵</i></b>")

    elif admin_case:

        await message.answer(f"Здравствуй, админ\n\n"
                             f"Что хочешь сделать сегодня? 💭"
                             f"\n\nДля справки нажмите <b><i>/help</i></b> 👈\n\n"
                             f"Для начала работы нажмите <b><i>/search</i></b> 👈\n\n"
                             f"----------Команды админа👇----------\n\n"
                             f"Забанить юзера - <b><i>/ban_user</i></b> 👈\n\n"
                             f"Разбанить юзера - <b><i>/unban_user</i></b> 👈\n\n"
                             f"Получить логи - <b><i>/get_logs</i></b> 👈\n\n"
                             f"json с юзерами - <b><i>/get_users_bd</i></b> 👈\n\n"
                             f"json с админами - <b><i>/get_admins_bd</i></b> 👈\n\n"
                             f"json с ban-юзерами - <b><i>/get_ban_users_bd</i></b>"
                             f"\n\n\n<b><i>made by <a href='https://t.me/kolo_id'>kolo</a></i></b>",
                             disable_web_page_preview=True)

    elif user_case:

        await message.answer(f"Здравствуй, я <b>ReAssembler</b>🤖\n\nБот для сбора информации"
                             f" из чатов и каналов в <b><i>Telegram</i></b> 💭"
                             f"\n\nДля справки нажмите <b><i>/help</i></b> 👈\n\n"
                             f"Для начала работы нажмите <b><i>/search</i></b>👈"
                             f"\n\n\n<b><i>made by <a href='https://t.me/kolo_id'>kolo</a></i></b>",
                             disable_web_page_preview=True)

    elif banned_user_case:

        await message.answer(f"Здравствуй, я <b>ReAssembler</b>🤖\n\nБот для сбора информации"
                             f" из чатов и каналов в <b><i>Telegram</i></b> 💭"
                             f"\n\n<u><b>Ты был заблокирован</b></u>"
                             f"\n\n\nПо поводу разбана - <a href='https://t.me/kolo_id'>kolo</a>",
                             disable_web_page_preview=True)

    await user_to_database(message)
