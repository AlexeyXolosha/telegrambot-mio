from aiogram import Router, F
from aiogram.types import Message

import keyboards.keyboards as kb

from aiogram.types import (ReplyKeyboardRemove)

router = Router()

@router.message(F.text == 'Расписание')
async def cmd_schedule(message: Message):
    await message.answer(f'Выберите день: ', reply_markup=kb.schedule)
    
@router.message(F.text == 'Понедельник')
async def schedule_mon(message: Message):
    await message.answer(f'🕐 <b>Время: </b>13:55 \n'
                         f'Предмет: Основы R (лек.),  Исмуратова А.М. , ст.пр. 239/2')
    await message.answer(f'🕐 <b>Время: </b>15:00 \n'
                         f'Предмет: Аналитика Big Data (лек.) Жусупова А.К., ст.пр. 302/2')   	
    await message.answer(f'🕐 <b>Время: </b>16:00 - 17:50 \n'
                         f'Предмет: Инструментальные средства разработки программ (пр.) Иванова И.В. ассоц. проф. 239/2', reply_markup=ReplyKeyboardRemove())   	
            
@router.message(F.text == 'Вторник')
async def schedule_mon(message: Message):
    await message.answer(f'🕐 <b>Время: </b>15:00 - 16:50 \n'
                         f'Предмет: Основы R (лаб.) Исмуратова А.М., ст.пр. 226/2')
    await message.answer(f'🕐 <b>Время: </b>17:00 - 18:50 \n'
                        f'Предмет: Инструментальные средства разработки программ (лаб.) Иванова И.В. ассоц. проф. 241/2', reply_markup=ReplyKeyboardRemove())
    
@router.message(F.text == 'Среда')
async def schedule_mon(message: Message):
    await message.answer(f'🕐 <b>Время: </b>09:00 - 09:50 \n'
                         f'Предмет: Электроника (лек.) Бермагамбетов А.К., ст.пр. 302/2	')
    await message.answer(f'🕐 <b>Время: </b>09:55 - 10.45 \n'
                         f'Предмет: Программирование на Python (лек.) Сатмаганбетова Ж.З., ст.пр. 302/2	')   	
    await message.answer(f'🕐 <b>Время: </b>11:00 - 11:50 \n'
                         f'Предмет: Серверное программирование (лек.) Сатмаганбетова Ж.З., ст.пр. 302/2', reply_markup=ReplyKeyboardRemove())  	
    
@router.message(F.text == 'Четверг')
async def schedule_mon(message: Message):
    await message.answer(f'🕐 <b>Время: </b>13:00 - 14:45 \n'
                         f'Предмет: Программирование на Python (лаб.) Сатмаганбетова Ж.З., ст.пр. 226/2')
    await message.answer(f'🕐 <b>Время: </b>15:00 - 16:50 \n'
                        f'Предмет: Аналитика Big Data (лаб.) Жусупова А.К., ст.пр. 239/2', reply_markup=ReplyKeyboardRemove())

    
@router.message(F.text == 'Пятница')
async def schedule_mon(message: Message):
    await message.answer(f'🕐 <b>Время: </b>15:00 - 16:50 \n'
                         f'Предмет: Электроника (лаб.) Бермагамбетов А.К., ст.пр. 231/2')
    await message.answer(f'🕐 <b>Время: </b>17:00 - 18:50 \n'
                        f'Предмет: Серверное программирование (лаб.) Сатмаганбетова Ж.З., ст.пр. 226/2', reply_markup=ReplyKeyboardRemove())    
    
    
    

