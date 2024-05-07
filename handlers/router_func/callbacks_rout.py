from aiogram import types
from aiogram.fsm.context import FSMContext
from handlers.router_func.rout_search import SearchState


async def callbacks_rout(callback: types.CallbackQuery, state: FSMContext) -> None:

    action: str = callback.data

    if action == "get_us_groups":

        await callback.message.answer('1. Get Users From Groups')
        await callback.message.answer('Enter link to channel')

        await callback.message.delete()

        await state.set_state(SearchState.waiting_for_get_participants_from_group)

    elif action == "get_us_channel":

        await callback.message.answer('2. Get Users From Channel')
        await callback.message.answer('Enter link to channel')

        await callback.message.delete()

        await state.set_state(SearchState.waiting_for_get_participants_from_channel)

    elif action == "get_mes_groups":

        await callback.message.answer('3. Get Messages From Groups')
        await callback.message.answer('Enter link to channel')

        await callback.message.delete()

        await state.set_state(SearchState.waiting_for_get_messages_from_group)

    elif action == "get_pos_channel":

        await callback.message.answer('4. Get Posts From Channel')
        await callback.message.answer('Enter link to channel')

        await callback.message.delete()

        await state.set_state(SearchState.waiting_for_get_posts_from_channel)

    elif action == "get_us_private_groups":

        await callback.message.answer('5. Get Users From Private Groups')
        await callback.message.answer('Enter invitation link to private chat')

        await callback.message.delete()

        await state.set_state(SearchState.waiting_for_get_users_from_private_group)

    elif action == "get_mes_private_groups":

        await callback.message.answer('6. Get Messages From Private Groups')
        await callback.message.answer('Enter invitation link to private chat')

        await callback.message.delete()

        await state.set_state(SearchState.waiting_for_get_messages_from_private_group)

    elif action == "get_inf_but":

        await callback.message.answer('<b>Information about button capabilities :</b>\n\n'
                                      '------------------------------------------------------------------\n'
                                      '\n<b>Get Users From Groups</b> -\n<i>Collecting information about members in the'
                                      'group\n</i>'
                                      '\n------------------------------------------------------------------\n'
                                      '\n<b>Get Users From Channel</b> -\n<i>Collecting information about channel '
                                      'subscribers\n</i>'
                                      '\n------------------------------------------------------------------\n'
                                      '\n<b>Get Messages From Group</b> -\n<i>Collecting messages in group</i>\n'
                                      '\n------------------------------------------------------------------\n'
                                      '\n<b>Get Posts From Channel</b> -\n<i>Collecting comments from channel\n</i>'
                                      '\n------------------------------------------------------------------\n\n'
                                      '<b>Get Users From Private Groups</b> -\n<i>Collecting information about '
                                      'members in private group\n</i>'
                                      '\n------------------------------------------------------------------\n\n'
                                      '<b>Get Messages From Private Groups</b> -\n<i>Collecting messages in a private '
                                      'group\n</i>'
                                      '\n------------------------------------------------------------------\n\n'
                                      '<i><b>The bot does not violate Telegram rules</b></i>')

    elif action == "get_big_inf":

        await callback.message.answer('<b>Privacy information :</b>\n\n'
                                      '------------------------------------------------------------------\n'
                                      '<i><b>This bot is designed to automate the collection of information:'
                                      ' collecting statistics, information about Telegram users and other information,'
                                      ' which can be collected using this bot, please read carefully before using it'
                                      'with the privacy policy Telegram, the bot developer is not responsible for'
                                      'possible use of this bot intruders</b></i>\n'
                                      '------------------------------------------------------------------\n\n'
                                      '<i><b>The bot does not violate Telegram rules</b></i>')

    elif action == "get_tech_inf":

        await callback.message.answer('<b>Technical information :</b>\n\n'
                                      '------------------------------------------------------------------\n'
                                      'The bot is written in a framework for <b>Python</b> - <i>aiogram v3.6.0</i>, '
                                      '<i>Telethon v1.35.0 library is used to collect information</i>\n\n'
                                      'Average waiting time for collecting information about participants from a chat '
                                      'with 1k participants - 3 seconds\n\n'
                                      'The current version of the bot does not collect images from posts in channels '
                                      'and in messages from chats\n\n'
                                      'The bot implements a hierarchy system, there is a role of the Creator, '
                                      'admins and for ordinary users, a user ban system is also implemented\n'
                                      '------------------------------------------------------------------\n\n'
                                      '<i><b>The bot does not violate Telegram rules</b></i>')
