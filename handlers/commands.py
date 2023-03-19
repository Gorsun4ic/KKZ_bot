from datetime import datetime

from aiogram import types, Router
from aiogram.filters import CommandObject
from aiogram.filters.command import Command

# Get current datetime
today = datetime.today().weekday()

router = Router()

# Command /start handler
@router.message(Command("start"))
async def command_start(message: types.Message):
    await message.answer(f"Вітаю вас @{message.from_user.username}")

# Command /developer handler
@router.message(Command("developer"))
async def command_developer(message: types.Message):
    await message.answer(
        'Я телеграм чат-бот Поціновувач ПЛС.\n'
        'Я був створений @Gorsun4ik для захоплення світу, але поки я просто чат-бот',
        parse_mode="html"
    )

# Command /schedule handler
@router.message(Command("schedule"))
async def command_schedule(message: types.Message, command: CommandObject):

    class_time = [
        "09:40-10:40",
        "10:50-11:50",
        "12:00-13:00",
        "13:10-14:10",
        "14:20-15:20",
        "15:30-16:30"
    ]

    class ScheduleFunction:
        async def tuesday(self):
            schedule = "<b>Розклад пар на вівторок:</b>\n\n"
            schedule += f"1: {class_time[0]} Диференціальні рівняння\n"
            schedule += f"2: {class_time[1]} Математичний аналіз\n"
            schedule += f"3: {class_time[2]} Технології\n"
            schedule += f"4: {class_time[3]} Алгоритми та структура даних\n"
            schedule += f"5: {class_time[4]} Історія: Україна і світ"
            await message.answer(schedule, parse_mode='html')

        async def wednesday(self):
            schedule = "<b>Розклад пар на середу:</b>\n\n"
            schedule += f"1: {class_time[1]} Географія, кабінет 413\n"
            schedule += f"2: {class_time[2]} Математика, кабінет 505\n"
            schedule += f"3: {class_time[3]} Алгоритми та структура даних, кабінет 201\n"
            schedule += f"4: {class_time[4]} Українська мова, кабінет 311\n"
            schedule += f"5: {class_time[5]} Українська література, кабінет 311\n"
            await message.answer(schedule, parse_mode='html')

        async def thursday(self):
            schedule = "<b>Розклад пар на четвер:</b>\n\n"
            schedule += f"1: {class_time[0]} Захист України, кабінет 001\n"
            schedule += f"2: {class_time[1]} Англійська, кабінет 420\n"
            schedule += f"3: {class_time[2]} Фіз-ра, спортзал\n"
            schedule += f"4: {class_time[3]} Фізика, кабінет 418\n"
            schedule += f"5: {class_time[4]} Математичний аналіз, кабінет 505"
            await message.answer(schedule, parse_mode='html')

        async def friday(self):
            schedule = "<b>Розклад пар на п'ятницю:</b>\n\n"
            schedule += f"1: {class_time[0]} Диференціальні рівняння, кабінет 212\n"
            schedule += f"2: {class_time[1]} Технології, кабінет 201\n"
            schedule += f"3: {class_time[2]} Технології, кабінет 201"
            await message.answer(schedule, parse_mode='html')

    schedule_obj = ScheduleFunction()

    if command.args == "понеділок" or command.args == "субота" or command.args == "неділя":
        await message.answer(
            "В цей день пар немає, гуляй.\n"
            "Якщо хочеш дізнатись розклад на якийсь день,\n"
            "напиши <code>/schedule день тижня</code>",
            parse_mode="html")

    elif command.args == "вівторок":
        await schedule_obj.tuesday()

    elif command.args == "середа":
        await schedule_obj.wednesday()

    elif command.args == "четвер":
        await schedule_obj.thursday()

    elif command.args == "п'ятниця" or command.args == "пятниця":
        await schedule_obj.friday()

    elif command.args == "тиждень" or command.args == "на тиждень" or command.args == "розклад на тиждень":
        await message.answer("<b>Розклад занять на тиждень:</b>\n", parse_mode="html")
        await schedule_obj.tuesday()
        await schedule_obj.wednesday()
        await schedule_obj.thursday()
        await schedule_obj.friday()

    else:
        # If today a weekend
        if today in [5, 6, 0]:
            await message.answer(
                "В цей день пар немає, гуляй.\n"
                "Якщо хочеш дізнатись розклад на якийсь день,\n"
                "напиши <code>/schedule день тижня</code>",
                parse_mode="html")

        if today == 1:
            await schedule_obj.tuesday()

        if today == 2:
            await schedule_obj.wednesday()

        if today == 3:
            await schedule_obj.thursday()

        if today == 4:
            await schedule_obj.friday()

# Command /help handler
@router.message(Command("help"))
async def command_help(message: types.Message):
    await message.answer(
        f"Вітаю @{message.from_user.username}, ось список моїх можливостей:\n"
        "<code>/start</code> - Привітатись з ботом\n"
        "<code>/schedule</code> - Дізнатись розклад пар\n"
        "<code>/developer</code> - Дізнатись про розробника бота\n"
        "<code>/help</code> - Список команд, власне ви вже використовуєте цю команду",
        parse_mode="html")
