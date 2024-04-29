import logging
from aiogram import types
from aiogram.fsm.context import FSMContext
from handlers.router_func.rout_search import SearchState
from handlers.router_func.action_0m_for_callback import action_0m_for_callback
from handlers.router_func.action_0p_for_callback import action_0p_for_callback


async def callbacks_rout(callback: types.CallbackQuery, state: FSMContext):

    action: str = callback.data

    if action == "get_us_groups":
        await callback.message.answer('Введите ссылку на чат')

        await state.set_state(SearchState.waiting_for_get_participants_of_group)

    elif action == "get_us_channel":
        await callback.message.answer('Введите ссылку на канал')

        await state.set_state(SearchState.waiting_for_get_participants_of_channel)

    elif action == "get_mes_groups":
        await callback.message.answer('Введите ссылку на чат')

        await state.set_state(SearchState.waiting_for_get_messages_of_group)

    elif action == "get_pos_channel":
        await callback.message.answer('Введите ссылку на канал')

        await state.set_state(SearchState.waiting_for_get_posts_of_channel)

    elif action[-2:] == "0p":

        try:

            await action_0p_for_callback(callback, action)

        except Exception as e:

            logging.error(e)

            await callback.message.answer('Некорректная ссылка')

        finally:

            await state.clear()

    elif action[-2:] == "0m":

        try:

            await action_0m_for_callback(callback, action)

        except Exception as e:

            logging.error(e)

            await callback.message.answer('Некорректная ссылка')

        finally:

            await state.clear()

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

        await callback.message.answer('Введите ссылку на чат')
