import asyncio

from aiogram import types
from aiogram.fsm.context import FSMContext
from functions.hand_search import SearchState
from functions.dump_all_participants import dump_all_participants


async def dp_handlers(dp):
    @dp.callback_query()
    async def callbacks(callback: types.CallbackQuery, state: FSMContext):
        action = callback.data

        if action == "get_us_groups":
            await callback.message.answer('Введите ссылку на чат')

            await state.set_state(SearchState.waiting_for_search_participants)

        elif action == "get_us_channel":
            await callback.message.answer('Введите ссылку на чат')

            await state.set_state(SearchState.waiting_for_get_messages)

        elif action == "get_inf_but":

            await callback.message.answer('<b>Информация о возможностях кнопок :</b>\n\n'
                                          '------------------------------------------------------------------\n'
                                          '<b>Get Users From Groups</b> -- сбор информации об участниках в группе\n'
                                          '------------------------------------------------------------------\n'
                                          '<b>Get Users From Channel</b> -- сбор информации о подписчиках канала\n'
                                          '------------------------------------------------------------------\n'
                                          '<b>Get Messages From Group</b> -- сбор сообщений в группе\n'
                                          '------------------------------------------------------------------\n'
                                          '<b>Get Messages From Channel</b> -- сбор комментариев из канала\n'
                                          '------------------------------------------------------------------\n\n'
                                          '<i><b>Бот не нарушает правил Telegram</b></i>')

        elif action == "get_big_inf":

            await callback.message.answer('<b>Информация о конфиденциальности :</b>\n\n'
                                          '------------------------------------------------------------------\n'
                                          '<i><b>Данный бот создан для автоматизации сбора информации:'
                                          ' сбор статистики, информации о пользователях Telegram и прочей информации,'
                                          ' которую можно добыть с помощью'
                                          ' этого бота, перед использованием внимательно ознакомьтесь'
                                          ' с политикой конфиденциальности'
                                          ' Telegram, разработчик бота не несёт ответственность за'
                                          ' возможное использование этого бота'
                                          ' злоумышленниками\n'
                                          '----------------------------------------------------------\n\n'
                                          'Бот не нарушает правил Telegram</b></i>')

        elif action == "get_tech_inf":

            await callback.message.answer('Введите ссылку на чат')

        elif action == "get_all_inf":

            await callback.message.answer('Введите ссылку на чат')

    @dp.message(SearchState.waiting_for_search_participants)
    async def get_url_for_users_in_groups(message: types.Message, state: FSMContext):

        if message.text.startswith('t.me') or message.text.startswith('https://t.me'):

            loop = asyncio.get_event_loop()
            loop.run_until_complete(dump_all_participants(message.text))

            await state.clear()

        else:

            await message.answer('this is not link')

            await state.clear()

    @dp.message(SearchState.waiting_for_get_messages)
    async def get_url_for_messages_in_groups(message: types.Message, state: FSMContext):

        await message.answer('444' + message.text)

        await state.clear()
