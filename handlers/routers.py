from aiogram import types, F
from aiogram.fsm.context import FSMContext
from handlers.router_func.rout_search import SearchState, AdminState, button_to_search_rout
from handlers.router_func.rout_help import button_to_help_rout
from handlers.router_func.rout_start import start_rout
from handlers.router_func.callbacks_rout import callbacks_rout
from handlers.router_func.wait_users_group_rout import get_url_for_users_in_groups_rout
from handlers.router_func.wait_users_channel_rout import get_url_for_users_in_channel_rout
from handlers.router_func.wait_messages_group_rout import get_url_for_messages_in_group_rout
from handlers.router_func.wait_posts_channel_rout import get_url_for_posts_in_channel_rout
from handlers.admin_router_func.add_admin_rout import add_admin_rout
from handlers.admin_router_func.del_admin_rout import del_admin_rout
from handlers.admin_router_func.ban_user_rout import ban_user_rout
from handlers.admin_router_func.unban_user_rout import unban_user_rout
from handlers.admin_router_func.wait_username_add_admin import get_username_for_add_admin_rout
from handlers.admin_router_func.wait_username_del_admin import get_username_for_del_admin_rout
from handlers.admin_router_func.wait_username_ban_user import get_username_for_ban_user_rout
from handlers.admin_router_func.wait_username_unban_user import get_username_for_unban_user_rout
from handlers.admin_router_func.get_logs_rout import get_logs_rout
from handlers.admin_router_func.get_bd_with_admins import get_admin_bd_rout
from handlers.admin_router_func.get_bd_with_users import get_users_bd_rout
from handlers.admin_router_func.get_bd_with_ban_users import get_ban_users_bd_rout
from handlers.admin_router_func.drop_data import drop_data_rout
from aiogram import Router
from aiogram.filters import Command


router: Router = Router()


@router.message(Command('start'))
async def start_routing(message: types.Message):

    await start_rout(message)


@router.message(Command('help'))
async def help_routing(message: types.Message):

    await button_to_help_rout(message)


@router.message(Command('search'))
async def search_routing(message: types.Message):

    await button_to_search_rout(message)


@router.message(Command('add_admin'))
async def add_admin_routing(message: types.Message, state: FSMContext):

    await add_admin_rout(message, state)


@router.message(Command('del_admin'))
async def del_admin_routing(message: types.Message, state: FSMContext):

    await del_admin_rout(message, state)


@router.message(Command('ban_user'))
async def ban_user_routing(message: types.Message, state: FSMContext):

    await ban_user_rout(message, state)


@router.message(Command('unban_user'))
async def unban_user_routing(message: types.Message, state: FSMContext):

    await unban_user_rout(message, state)


@router.message(Command('get_logs'))
async def get_logs_routing(message: types.Message):

    await get_logs_rout(message)


@router.message(Command('get_admins_bd'))
async def get_admin_bd_routing(message: types.Message):

    await get_admin_bd_rout(message)


@router.message(Command('get_users_bd'))
async def get_users_bd_routing(message: types.Message):

    await get_users_bd_rout(message)


@router.message(Command('get_ban_users_bd'))
async def get_ban_users_bd_routing(message: types.Message):

    await get_ban_users_bd_rout(message)


@router.message(F.text == 'drop data')
async def drop_data_routing(message: types.Message):

    await drop_data_rout(message)


@router.callback_query()
async def callbacks_routing(callback: types.CallbackQuery, state: FSMContext):

    await callbacks_rout(callback, state)


@router.message(SearchState.waiting_for_get_participants_of_group)
async def get_url_for_users_in_groups(message: types.Message, state: FSMContext):

    await get_url_for_users_in_groups_rout(message, state)


@router.message(SearchState.waiting_for_get_participants_of_channel)
async def get_url_for_users_in_channel(message: types.Message, state: FSMContext):

    await get_url_for_users_in_channel_rout(message, state)


@router.message(SearchState.waiting_for_get_messages_of_group)
async def get_url_for_messages_in_group(message: types.Message, state: FSMContext):

    await get_url_for_messages_in_group_rout(message, state)


@router.message(SearchState.waiting_for_get_posts_of_channel)
async def get_url_for_messages_in_group(message: types.Message, state: FSMContext):

    await get_url_for_posts_in_channel_rout(message, state)


@router.message(AdminState.waiting_for_add_admin)
async def get_username_for_add_admin(message: types.Message, state: FSMContext):

    await get_username_for_add_admin_rout(message, state)


@router.message(AdminState.waiting_for_del_admin)
async def get_username_for_del_admin(message: types.Message, state: FSMContext):

    await get_username_for_del_admin_rout(message, state)


@router.message(AdminState.waiting_for_ban_user)
async def get_username_for_ban_user(message: types.Message, state: FSMContext):

    await get_username_for_ban_user_rout(message, state)


@router.message(AdminState.waiting_for_unban_user)
async def get_username_for_unban_user(message: types.Message, state: FSMContext):

    await get_username_for_unban_user_rout(message, state)


@router.message()
async def unknown_command(message: types.Message):

    await message.answer('Unknown command\n'
                         'Enter /help to get help')
