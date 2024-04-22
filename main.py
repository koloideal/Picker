from aiogram import Bot, Dispatcher
import asyncio
import configparser
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums.parse_mode import ParseMode
from handlers.hand_start import start
from handlers.hand_search import search
from handlers.hand_help import helper
from handlers.dp_handlers import dp_handlers
from aiogram.filters.command import Command
import os

config = configparser.ConfigParser()
config.read('secret_data/config.ini')

bot_token = config.get('Telegram', 'bot_token')

storage: MemoryStorage = MemoryStorage()

bot: Bot = Bot(token=bot_token, parse_mode=ParseMode('HTML'))
dp: Dispatcher = Dispatcher(storage=storage)

os.makedirs('users_of_groups_to_json', exist_ok=True)


async def main() -> None:

    dp.message.register(start, Command('start'))
    dp.message.register(search, Command('search'))
    dp.message.register(helper, Command('help'))

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(dp_handlers(dp))

    asyncio.run(main())
