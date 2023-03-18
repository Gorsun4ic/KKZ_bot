import asyncio
import logging
from datetime import datetime

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandObject
from aiogram.filters.command import Command

from config_reader import config


def main():
    pass


# Power on logging to unskip important mesages
logging.basicConfig(level=logging.INFO)
# Bot's object
bot = Bot(token=config.bot_token.get_secret_value())
# Dispatcher
dp = Dispatcher()

# Get current datetime
today = datetime.today().weekday()

# Command /start handler
@dp.message(Command("developer"))
async def command_developer(message: types.Message):
    await message.answer(
        'Я телеграм чат-бот Поціновувач ПЛС.\n'
        'Я був створений @Gorsun4ik для захоплення світу, але поки я просто чат-бот',
        parse_mode="html"
    )


# Command /developer handler
@dp.message(Command("start"))
async def command_start(message: types.Message):
    await message.answer(f"Вітаю вас @{message.from_user.username}")


# Command /schedule handler
@dp.message(Command("schedule"))
async def command_schedule(message: types.Message, command: CommandObject):
    class ScheduleFunction:
        async def tuesday(self):
            schedule = "<b>Розклад пар на вівторок:</b>\n\n"
            schedule += "1: 9:40-10:40 Диференціальні рівняння\n"
            schedule += "2: 10:50-11:50 Математичний аналіз\n"
            schedule += "3: 12:00-13:00 Технології\n"
            schedule += "4: 13:10-14:10 Алгоритми та структура даних\n"
            schedule += "5: 14:20-15:20 Історія: Україна і світ"
            await message.answer(schedule, parse_mode='html')

        async def wednesday(self):
            schedule = "<b>Розклад пар на середу:</b>\n\n"
            schedule += "1: 10:50-11:50 Географія, кабінет 413\n"
            schedule += "2: 12:00-13:00 Математи, кабінет 505\n"
            schedule += "3: 13:10-14:10 Алгоритми та структура даних, кабінет 201\n"
            schedule += "4: 14:20-15:20 Українська мова, кабінет 311\n"
            schedule += "4: 14:20-15:20 Українська література, кабінет 311\n"
            await message.answer(schedule, parse_mode='html')

        async def thursday(self):
            schedule = "<b>Розклад пар на четвер:</b>\n\n"
            schedule += "1: 9:40-10:40 Англійська, кабінет 420\n"
            schedule += "2: 10:50-11:50 Фіз-ра, спортзал\n"
            schedule += "3: 12:00-13:00 Фізика, кабінет 418\n"
            schedule += "4: 13:10-14:10 Математичний аналіз, кабінет 505"
            await message.answer(schedule, parse_mode='html')

        async def friday(self):
            schedule = "<b>Розклад пар на п'ятницю:</b>\n\n"
            schedule += "1: 9:40-10:40 Диференціальні рівняння, кабінет 212\n"
            schedule += "2: 10:50-11:50 Технології, кабінет 201\n"
            schedule += "3: 12:00-13:00 Технології, кабінет 201"
            await message.answer(schedule, parse_mode='html')

    schedule_obj = ScheduleFunction()

    if command.args == "понеділок" or command.args == "субота" or command.args == "неділя":
        await message.answer("В цей день пар немає, гуляй.\n"
                             "Якщо хочеш дізнатись розклад на якийсь день,\n"
                             "напиши <code>/schedule день тижня</code>", parse_mode="html")

    elif command.args == "вівторок":
        await schedule_obj.tuesday()

    elif command.args == "середа":
        await schedule_obj.wednesday()

    elif command.args == "четвер":
        await schedule_obj.thursday()

    elif command.args == "п'ятниця" or command.args == "пятниця":
        await schedule_obj.friday()

    else:
        # If today a weekend
        if today in [5, 6, 0]:
            await message.answer("В цей день пар немає, гуляй.\n"
                                 "Якщо хочеш дізнатись розклад на якийсь день,\n"
                                 "напиши <code>/schedule день тижня</code>", parse_mode="html")

        if today == 1:
            await schedule_obj.tuesday()

        if today == 2:
            await schedule_obj.wednesday()

        if today == 3:
            await schedule_obj.thursday()

        if today == 4:
            await schedule_obj.friday()

# Command /help handler
@dp.message(Command("help"))
async def command_help(message: types.Message):
    await message.answer(f"Вітаю @{message.from_user.username}, ось список моїх можливостей:\n"
                         "<code>/start</code> - Привітатись з ботом\n"
                         "<code>/schedule</code> - Дізнатись розклад пар\n"
                         "<code>/developer</code> - Дізнатись про розробника бота\n"
                         "<code>/help</code> - Список команд, власне ви вже використовуєте цю команду", parse_mode="html")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
