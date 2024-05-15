import os
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from configparser import ConfigParser
from aiogram import Bot, Dispatcher
from telethon import TelegramClient
import asyncio
import logging

config: ConfigParser = ConfigParser()
config.read('secret_data/config.ini')

bot_token: str = config.get('Telegram', 'bot_token')
api_id: int = int(config['Telegram']['api_id'])
api_hash: str = config['Telegram']['api_hash']


client: TelegramClient = TelegramClient('session', api_id, api_hash)
client.start()
client.disconnect()

storage: MemoryStorage = MemoryStorage()

bot: Bot = Bot(token=bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp: Dispatcher = Dispatcher(storage=storage)

os.makedirs('content', exist_ok=True)
os.makedirs('database', exist_ok=True)


async def main() -> None:

    from handlers.routers import router

    logging.warning('Starting bot...')
    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":

    try:

        print("\n\033[1m\033[30m\033[44m {} \033[0m".format("Starting bot..."))

        logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.WARNING,
                            filename='secret_data/logs.txt',
                            filemode='a',
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s\n\n\n')

        asyncio.run(main())

    except KeyboardInterrupt:

        print("\n\033[1m\033[30m\033[45m {} \033[0m".format("End of work..."))

        logging.warning('End of work...')

        exit()
