from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from configparser import ConfigParser
from aiogram import Bot, Dispatcher
from handlers.routers import router
import asyncio
import logging
import os


config: ConfigParser = ConfigParser()
config.read('secret_data/config.ini')

bot_token: str = config.get('Telegram', 'bot_token')

storage: MemoryStorage = MemoryStorage()

bot: Bot = Bot(token=bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp: Dispatcher = Dispatcher(storage=storage)

os.makedirs('users_of_groups_to_json', exist_ok=True)
os.makedirs('users_of_channels_to_json', exist_ok=True)
os.makedirs('messages_of_groups_to_json', exist_ok=True)
os.makedirs('posts_of_channel_to_json', exist_ok=True)
os.makedirs('database', exist_ok=True)


async def main() -> None:

    logging.warning(f'Starting bot...')

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
