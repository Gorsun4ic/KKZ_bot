import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config_reader import config
from handlers import commands


# Power on polling and new updates
async def main():
    # Power on logging to unskip important mesages
    logging.basicConfig(level=logging.INFO)

    # Bot's object
    bot = Bot(token=config.bot_token.get_secret_value())

    # Dispatcher
    dp = Dispatcher()

    admin = config.admin_id.get_secret_value()

    dp.include_router(commands.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
