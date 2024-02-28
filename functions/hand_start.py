from aiogram import types
from functions.user_to_database import user_to_database


async def start_command(message: types.Message) -> None:

    await message.answer(f"Здраствуй, я <b>ReAssembler</b>\n\nБот для сбора информации"
                         f" из чатов и каналов в <b><i>Telegram</i></b>\n\nДля ознакомления с моими возможностями"
                         f" нажмите <b><i>/search</i></b>\n\n<i>made by <a href='tg://user?id=2047958833'>kolo</a></i>")

    await user_to_database(message)


