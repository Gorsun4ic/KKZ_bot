import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_reader import config
from handlers import commands


# Запуск процесса поллинга новых апдейтов
async def main():
    # Power on logging to unskip important mesages
    logging.basicConfig(level=logging.INFO)
    # Bot's object
    bot = Bot(token=config.bot_token.get_secret_value())
    # Dispatcher
    dp = Dispatcher()

    dp.include_router(commands.router)


    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
