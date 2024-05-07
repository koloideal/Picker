from aiogram import types
from handlers.router_func.rout_search import AdminState
from aiogram.fsm.context import FSMContext
from database_func.get_admins import get_admins


async def ban_user_rout(message: types.Message, state: FSMContext) -> None:

    user_id: int = message.from_user.id

    admins_id: list = await get_admins()

    if user_id != 2047958833 and user_id not in admins_id:

        await message.answer('Unknown command, enter /help')

    else:

        await message.answer('Enter a username')

        await state.set_state(AdminState.waiting_for_ban_user)

    return
