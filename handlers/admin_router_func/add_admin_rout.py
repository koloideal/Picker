from aiogram import types
from handlers.router_func.rout_search import AdminState
from aiogram.fsm.context import FSMContext


async def add_admin_rout(message: types.Message, state: FSMContext) -> None:

    user_id: int = message.from_user.id

    if user_id != 2047958833:

        await message.answer('Unknown command, enter /help')

    else:

        await message.answer('Enter a username')

        await state.set_state(AdminState.waiting_for_add_admin)

    return
