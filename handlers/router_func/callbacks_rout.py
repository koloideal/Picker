from aiogram import types
from aiogram.fsm.context import FSMContext
from handlers.router_func.rout_search import SearchState


async def callbacks_rout(callback: types.CallbackQuery, state: FSMContext):

    action: str = callback.data

    if action == "get_us_groups":

        await callback.message.answer('Введите ссылку на чат')

        await callback.message.delete()

        await state.set_state(SearchState.waiting_for_get_participants_from_group)

    elif action == "get_us_channel":

        await callback.message.answer('Введите ссылку на канал')

        await callback.message.delete()

        await state.set_state(SearchState.waiting_for_get_participants_from_channel)

    elif action == "get_mes_groups":

        await callback.message.answer('Введите ссылку на чат')

        await callback.message.delete()

        await state.set_state(SearchState.waiting_for_get_messages_from_group)

    elif action == "get_pos_channel":

        await callback.message.answer('Введите ссылку на канал')

        await callback.message.delete()

        await state.set_state(SearchState.waiting_for_get_posts_from_channel)

    elif action == "get_mes_private_groups":

        await callback.message.answer('Введите пригласительную ссылку на приватный чат')

        await callback.message.delete()

        await state.set_state(SearchState.waiting_for_get_users_from_private_group)

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
                                      ' которую можно собрать с помощью'
                                      ' этого бота, перед использованием внимательно ознакомьтесь'
                                      ' с политикой конфиденциальности'
                                      ' Telegram, разработчик бота не несёт ответственность за'
                                      ' возможное использование этого бота'
                                      ' злоумышленниками\n'
                                      '------------------------------------------------------------------\n\n'
                                      'Бот не нарушает правил Telegram</b></i>')

    elif action == "get_tech_inf":

        await callback.message.answer('<b>Техническая информация :</b>\n\n'
                                      '------------------------------------------------------------------\n'
                                      'Бот написан на фреймворке для <b>Python</b> - <i>aiogram v3.5.0</i>, для '
                                      'сбора информации используется библиотека <i>Telethon v1.35.0</i>\n\n'
                                      'Среднее время ожидания сбора информации об участниках из чата с 1к участников'
                                      ' - 3 секунды\n\n'
                                      'В актуальной версии бота не собираются изображение из постов в каналах и в'
                                      ' сообщениях из чатов\n\n'
                                      'В боте реализована система иерархии, присутствует роль Создателя, админов и '
                                      'обычных юзеров, также реализована система бана пользователей\n'
                                      '------------------------------------------------------------------\n\n'
                                      '<i><b>Бот не нарушает правил Telegram</b></i>')
