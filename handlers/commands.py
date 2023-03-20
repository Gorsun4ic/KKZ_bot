from datetime import datetime

from aiogram import types, Router
from aiogram.filters import CommandObject, Text
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# # Get current datetime
today = datetime.today().weekday()

class_time = [
    "09:40-10:40",
    "10:50-11:50",
    "12:00-13:00",
    "13:10-14:10",
    "14:20-15:20",
    "15:30-16:30"
]


class ScheduleFunction:
    async def tuesday(self, message: types.Message, call: types.CallbackQuery):
        schedule = "<b>Розклад пар на вівторок:</b>\n\n"
        schedule += f"1: {class_time[0]} Диференціальні рівняння\n"
        schedule += f"2: {class_time[1]} Математичний аналіз\n"
        schedule += f"3: {class_time[2]} Технології\n"
        schedule += f"4: {class_time[3]} Алгоритми та структура даних\n"
        schedule += f"5: {class_time[4]} Історія: Україна і світ"
        if call:
            await call.message.answer(schedule, parse_mode='html')
        else:
            await message.answer(schedule, parse_mode='html')

    async def wednesday(self, message: types.Message, call: types.CallbackQuery):
        schedule = "<b>Розклад пар на середу:</b>\n\n"
        schedule += f"1: {class_time[1]} Географія, кабінет 413\n"
        schedule += f"2: {class_time[2]} Математика, кабінет 505\n"
        schedule += f"3: {class_time[3]} Алгоритми та структура даних, кабінет 201\n"
        schedule += f"4: {class_time[4]} Українська мова, кабінет 311\n"
        schedule += f"5: {class_time[5]} Українська література, кабінет 311\n"
        if call:
            await call.message.answer(schedule, parse_mode='html')
        else:
            await message.answer(schedule, parse_mode='html')

    async def thursday(self, message: types.Message, call: types.CallbackQuery):
        schedule = "<b>Розклад пар на четвер:</b>\n\n"
        schedule += f"1: {class_time[0]} Захист України, кабінет 001\n"
        schedule += f"2: {class_time[1]} Англійська, кабінет 420\n"
        schedule += f"3: {class_time[2]} Фіз-ра, спортзал\n"
        schedule += f"4: {class_time[3]} Фізика, кабінет 418\n"
        schedule += f"5: {class_time[4]} Математичний аналіз, кабінет 505"
        if call:
            await call.message.answer(schedule, parse_mode='html')
        else:
            await message.answer(schedule, parse_mode='html')

    async def friday(self, message: types.Message, call: types.CallbackQuery):
        schedule = "<b>Розклад пар на п'ятницю:</b>\n\n"
        schedule += f"1: {class_time[0]} Диференціальні рівняння, кабінет 212\n"
        schedule += f"2: {class_time[1]} Технології, кабінет 201\n"
        schedule += f"3: {class_time[2]} Технології, кабінет 201"
        if call:
            await call.message.answer(schedule, parse_mode='html')
        else:
            await message.answer(schedule, parse_mode='html')

    async def week(self, message: types.Message, call: types.CallbackQuery):
        if call:
            await call.message.answer("Розклад занять на тиждень:\n")
        else:
            await message.answer("Розклад занять на тиждень:\n")

        await schedule_obj.tuesday(message, call)
        await schedule_obj.wednesday(message, call)
        await schedule_obj.thursday(message, call)
        await schedule_obj.friday(message, call)

    async def weekend(self, message: types.Message):
        await message.answer(
            "В цей день пар немає, гуляй.\n"
            "Якщо хочеш дізнатись розклад на якийсь день,\n"
            "напиши <code>/schedule день тижня</code>",
            parse_mode="html")

router = Router()

schedule_obj = ScheduleFunction()


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
    command_args = message.text.split()

    # Define buttons for Tuesday to Friday
    button_mon = InlineKeyboardButton(text='Понеділок', callback_data='schedule_monday')
    button_tue = InlineKeyboardButton(text='Вівторок', callback_data='schedule_tuesday')
    button_wed = InlineKeyboardButton(text='Середа', callback_data='schedule_wednesday')
    button_thu = InlineKeyboardButton(text='Четвер', callback_data='schedule_thursday')
    button_fri = InlineKeyboardButton(text="П'ятниця", callback_data='schedule_friday')
    button_sat = InlineKeyboardButton(text='Субота', callback_data='schedule_saturday')
    button_sun = InlineKeyboardButton(text="Неділя", callback_data='schedule_sunday')
    button_week = InlineKeyboardButton(text="На тиждень", callback_data='schedule_week')

    # Add buttons to keyboard
    schedule_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[button_mon], [button_tue],
                         [button_wed], [button_thu],
                         [button_fri], [button_sat],
                         [button_sun], [button_week]])

    if len(command_args) > 1:
        for day in command_args[1:]:
            day = day.lower()
        if day == "вівторок" or day == "на вівторок":
            await schedule_obj.tuesday(message, False)
        elif day == "середа" or day == "на середу":
            await schedule_obj.wednesday(message, False)
        elif day == "четвер" or day == "на четвер":
            await schedule_obj.thursday(message, False)
        elif day == "п'ятниця" or day == "пятниця" or day == "на п'ятницю" or day == "на пятницю":
            await schedule_obj.friday(message, False)
        elif day == "тиждень" or day == "на тиждень" or day == "розклад на тиждень":
            await schedule_obj.week(message, False)
        elif day == "завтра" or day == "на завтра":
            if today == 4 or today == 5 or today == 6:
                await schedule_obj.weekend(message)
            elif today == 0:
                await schedule_obj.tuesday(message, False)
            elif today == 1:
                await schedule_obj.wednesday(message, False)
            elif today == 2:
                await schedule_obj.thursday(message, False)
            elif today == 3:
                await schedule_obj.friday(message, False)
        elif day == "вчора" or day == "на вчора":
            if today == 0 or today == 1 or today == 6:
                await schedule_obj.weekend(message )
            elif today == 2:
                await schedule_obj.tuesday(message, False)
            elif today == 3:
                await schedule_obj.wednesday(message, False)
            elif today == 4:
                await schedule_obj.thursday(message, False)
            elif today == 5:
                await schedule_obj.friday(message, False)
        elif day == "сьогодні" or day == "на сьогодні":
            if today == 0 or today == 5 or today == 6:
                await schedule_obj.weekend(message )
            elif today == 1:
                await schedule_obj.tuesday(message, False)
            elif today == 2:
                await schedule_obj.wednesday(message, False)
            elif today == 3:
                await schedule_obj.thursday(message, False)
            elif today == 4:
                await schedule_obj.friday(message, False)
        else:
            await schedule_obj.weekend(message)

    else:
        # Send message with keyboard
        await message.answer("Виберіть день тижня, на який ви хочете дізнатись розклад:",
                             reply_markup=schedule_keyboard)


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


@router.callback_query(Text(startswith="schedule_"))
async def command_schedule_callback(call: types.CallbackQuery):
    action = call.data
    await call.answer()

    if action == "schedule_monday" or action == "schedule_saturday" or action == "schedule_sunday":
        await call.message.answer(
            "В цей день пар немає, гуляй.\n"
            "Якщо хочеш дізнатись розклад на якийсь день,\n"
            "напиши <code>/schedule день тижня</code>",
            parse_mode="html"
        )

    elif action == "schedule_tuesday":
        await schedule_obj.tuesday(None, call)

    elif action == "schedule_wednesday":
        await schedule_obj.wednesday(None, call)

    elif action == "schedule_thursday":
        await schedule_obj.thursday(None, call)

    elif action == "schedule_friday":
        await schedule_obj.friday(None, call)

    elif action == "schedule_week":
        await schedule_obj.week(None, call)
