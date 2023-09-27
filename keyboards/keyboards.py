#Создаем отдельный файл для работы с клавиатурой
#Импортируем из aiogram нужные нам методы

from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardButton, InlineKeyboardMarkup)


main_kb = [
    [KeyboardButton(text= 'Новости в мире игр')],
    [KeyboardButton(text= 'Расписание')],
]

main = ReplyKeyboardMarkup(keyboard=main_kb, resize_keyboard=True, input_field_placeholder="Выберите пункт ниже")


schedule_kb = [
    [KeyboardButton(text ="Понедельник")],
    [KeyboardButton(text ="Вторник")],
    [KeyboardButton(text ="Среда")],
    [KeyboardButton(text ="Четверг")],
    [KeyboardButton(text ="Пятница")]
]
schedule = ReplyKeyboardMarkup(keyboard=schedule_kb, resize_keyboard=True, input_field_placeholder="Выберите пункт ниже")
