from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from handlers.hand_search import SearchState
from get_data_telegram.get_users_from_groups import get_users_from_groups
from get_data_telegram.get_users_from_channel import get_users_from_channel
import os


async def dp_handlers(dp):
    @dp.callback_query()
    async def callbacks(callback: types.CallbackQuery, state: FSMContext):
        action: str = callback.data

        if action == "get_us_groups":
            await callback.message.answer('Введите ссылку на чат')

            await state.set_state(SearchState.waiting_for_search_participants_of_group)

        elif action == "get_us_channel":
            await callback.message.answer('Введите ссылку на канал')

            await state.set_state(SearchState.waiting_for_search_participants_of_channel)

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
                                          '------------------------------------------------------------------\n\n'
                                          'Бот не нарушает правил Telegram</b></i>')

        elif action == "get_tech_inf":

            await callback.message.answer('Введите ссылку на чат')

        elif action == "get_all_inf":

            await callback.message.answer('Введите ссылку на чат')

    @dp.message(SearchState.waiting_for_search_participants_of_group)
    async def get_url_for_users_in_groups(message: types.Message, state: FSMContext):

        if message.text.startswith('t.me') or message.text.startswith('https://t.me'):

            file_name: str = await get_users_from_groups(message.text)

            if file_name == '!ChatAdminRequiredError':

                await message.answer('Вы должны быть владельцем или админом данного канала')

                await state.clear()

            elif file_name == '!ValueError':

                await message.answer('Некорректная ссылка')

                await state.clear()

            else:

                full_file_name: str = f'users_of_groups_to_json/{file_name}.json'

                document: FSInputFile = FSInputFile(full_file_name)

                await message.answer_document(document=document)

                os.remove(full_file_name)

                await state.clear()

        else:

            await message.answer('This is not link')

            await state.clear()

    @dp.message(SearchState.waiting_for_search_participants_of_channel)
    async def get_url_for_users_in_channel(message: types.Message, state: FSMContext):

        if message.text.startswith('t.me') or message.text.startswith('https://t.me'):

            file_name: str = await get_users_from_channel(message.text)

            if file_name == '!ChatAdminRequiredError':

                await message.answer('Вы должны быть владельцем или админом данного канала')

                await state.clear()

            elif file_name == '!ValueError':

                await message.answer('Некорректная ссылка')

                await state.clear()

            else:

                full_file_name: str = f'users_of_channels_to_json/{file_name}.json'

                document: FSInputFile = FSInputFile(full_file_name)

                await message.answer_document(document=document)

                os.remove(full_file_name)

                await state.clear()

        else:

            await message.answer('This is not link')

            await state.clear()
