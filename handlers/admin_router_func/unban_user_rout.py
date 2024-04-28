from aiogram import types
from handlers.router_func.rout_search import AdminState
from aiogram.fsm.context import FSMContext
from database_func.get_admins import get_admins


async def unban_user_rout(message: types.Message, state: FSMContext):

    user_id = message.from_user.id

    admins_id = await get_admins()

    if user_id != 2047958833 and user_id not in admins_id:

        await message.answer('Unknown command\n'
                             'Enter /help to get help')

    else:

        await message.answer('Введи юзернейм')

        await state.set_state(AdminState.waiting_for_unban_user)
