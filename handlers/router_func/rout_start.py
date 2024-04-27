from aiogram import types
from utils_func.user_to_database import user_to_database
from utils_func.get_admins import get_admins


async def start_rout(message: types.Message) -> None:

    user_id: int = message.from_user.id

    admins_id: list = await get_admins()

    if user_id not in admins_id and user_id != 2047958833:

        await message.answer(f"Здравствуй, я <b>ReAssembler</b>🤖\n\nБот для сбора информации"
                             f" из чатов и каналов в <b><i>Telegram</i></b> 💭"
                             f"\n\nДля справки нажмите <b><i>/help</i></b> 👈\n\n"
                             f"Для начала работы нажмите <b><i>/search</i></b> 👈"
                             f"\n\n\n<b><i>made by <a href='https://t.me/kolo_id'>kolo</a></i></b> "
                             f"                                        •ᴗ•",
                             disable_web_page_preview=True)

    elif (user_id in admins_id and user_id == 2047958833) or user_id == 2047958833:

        await message.answer(f"Здравствуй, Создатель\n\n"
                             f"Что хочешь сделать сегодня? 💭"
                             f"\n\nДля справки нажмите <b><i>/help</i></b> 👈\n\n"
                             f"Для начала работы нажмите <b><i>/search</i></b> 👈\n\n"
                             f"------------Команды создателя👇------------\n\n"
                             f"Добавить админа - <b><i>/add_admin</i></b> 👈\n\n"
                             f"Удалить админа - <b><i>/del_admin</i></b> 👈\n\n"
                             f"Получить логи - <b><i>/get_logs</i></b> 👈\n\n"
                             f"Получить бд с юзерами - <b><i>/get_users_bd</i></b> 👈\n\n"
                             f"Получить бд с админами - <b><i>/get_admins_bd</i></b> 👈\n\n"
                             f"<strike>You know the rest</strike>"
                             f"\n\n\n<b><i>made by you 🫵</i></b>")

    elif user_id in admins_id and user_id != 2047958833:

        await message.answer(f"Здравствуй, админ\n\n"
                             f"Что хочешь сделать сегодня? 💭"
                             f"\n\nДля справки нажмите <b><i>/help</i></b> 👈\n\n"
                             f"Для начала работы нажмите <b><i>/search</i></b> 👈\n\n"
                             f"------------Команды админа👇------------\n\n"
                             f"Получить логи - <b><i>/get_logs</i></b> 👈\n\n"
                             f"Получить бд с юзерами - <b><i>/get_users_bd</i></b> 👈\n\n"
                             f"Получить бд с админами - <b><i>/get_admins_bd</i></b> 👈\n\n"
                             f"\n\n\n<b><i>made by <a href='https://t.me/kolo_id'>kolo</a></i></b>",
                             disable_web_page_preview=True)

    await user_to_database(message)
