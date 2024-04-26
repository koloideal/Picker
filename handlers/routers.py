from aiogram import types
from aiogram.fsm.context import FSMContext
from handlers.router_func.rout_search import SearchState, button_to_search_rout
from handlers.router_func.rout_help import button_to_help_rout
from handlers.router_func.rout_start import start_rout
from handlers.router_func.callbacks_rout import callbacks_rout
from handlers.router_func.wait_users_group_rout import get_url_for_users_in_groups_rout
from handlers.router_func.wait_users_channel_rout import get_url_for_users_in_channel_rout
from handlers.router_func.wait_messages_group_rout import get_url_for_messages_in_group_rout
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


@router.message()
async def unknown_command(message: types.Message):

    await message.answer('Unknown command\n'
                         'Enter /help to get help')
