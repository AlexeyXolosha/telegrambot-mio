import asyncio
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from parsing.stopgame import check_news
from aiogram.types import (ReplyKeyboardRemove)


import keyboards.keyboards as kb
import json

router = Router()

@router.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer(f'Приветствую, <b>{message.from_user.first_name}!</b> \n'
                         f'Если хочешь узнать побольше, <b>напиши команду /help </b>')

@router.message(F.text == '/help')
async def cmd_help(message: Message):
    await message.answer(f'<b>Приветствую вас, товарищ! Тебе нужна помощь?</b>'
                         f' Тогда лови доступные команды: \n' 
                         f' /start - Запустить бота \n'
                         f' /help - Доступные команды \n'
                         f' /menu - Открыть меню \n'
                         f' /weather - Узнать погоду в вашем городе')


#Новости 
@router.message(F.text == '/menu')
async def cmd_menu(message: Message):
    await message.answer('Меню открыто.', reply_markup=kb.main)
 
@router.message(F.text == 'Новости в мире игр')
async def cmd_newsg(message: Message):
    with open("news_dict.json", encoding="utf-8") as file:
        news_dict = json.load(file)
        fresh_news = check_news()
     
        if len(fresh_news)>1:
            for k, v in sorted(fresh_news.items())[-5:]:
                news = (f"{v['article_title']} \n"
                    f"{v['article_href']}")
                await message.answer(news)
        else:
            for k, v in sorted(news_dict.items())[-5:]:
                news = (f"{v['article_title']} \n"
                    f"{v['article_href']}")
                await message.answer(news,  reply_markup=ReplyKeyboardRemove())
            
         












    