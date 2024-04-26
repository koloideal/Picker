from aiogram import types
from utils_func.user_to_database import user_to_database


async def start_rout(message: types.Message) -> None:

    await message.answer(f"Здравствуй, я <b>ReAssembler</b>🤖\n\nБот для сбора информации"
                         f" из чатов и каналов в <b><i>Telegram</i></b> 💭"
                         f"\n\nДля справки нажмите <b><i>/help</i></b> 👈\n\n"
                         f"Для начала работы нажмите <b><i>/search</i></b> 👈"
                         f"\n\n\n<b><i>made by <a href='https://t.me/kolo_id'>kolo</a></i></b> "
                         f"                                        •ᴗ•",
                         disable_web_page_preview=True)

    await user_to_database(message)
