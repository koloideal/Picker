from aiogram import Bot, Dispatcher
import asyncio
import configparser
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums.parse_mode import ParseMode
from functions.hand_start import start_command
from aiogram.filters.command import Command


config = configparser.ConfigParser()
config.read('C:\\Python_Projects\\ReAssembler\\utils\\config.ini')

bot_token = config['Telegram']['bot_token']

storage: MemoryStorage = MemoryStorage()

bot: Bot = Bot(token=bot_token, parse_mode=ParseMode('HTML'))
dp: Dispatcher = Dispatcher(storage=storage)


async def main() -> None:

    dp.message.register(start_command, Command('start'))

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, mylist=[1, 2, 3])


if __name__ == "__main__":

    asyncio.run(main())
