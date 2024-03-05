from aiogram import Bot, Dispatcher
import asyncio
import configparser
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums.parse_mode import ParseMode
from functions.hand_start import start
from functions.hand_search import search
from functions.hand_help import helper
from functions.dp_handlers import dp_handlers
from aiogram.filters.command import Command


config = configparser.ConfigParser()
config.read('C:\\Python_Projects\\ReAssembler\\utils\\config.ini')

bot_token = config['Telegram']['bot_token']

storage: MemoryStorage = MemoryStorage()

bot: Bot = Bot(token=bot_token, parse_mode=ParseMode('HTML'))
dp: Dispatcher = Dispatcher(storage=storage)


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
