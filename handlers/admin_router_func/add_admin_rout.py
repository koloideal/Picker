from aiogram import types
from handlers.router_func.rout_search import AdminState
from aiogram.fsm.context import FSMContext


async def add_admin_rout(message: types.Message, state: FSMContext):

    user_id = message.from_user.id

    if user_id != 2047958833:

        await message.answer('Unknown command\n'
                             'Enter /help to get help')

    else:

        await message.answer('Введи юзернейм')

        await state.set_state(AdminState.waiting_for_add_admin)
