import asyncio
from aiogram import Bot, Dispatcher

#прописываем router для объединение handlers
from app import heandlers, heandlers_schedule
from app import handlers_none

#Для Token
from dotenv import load_dotenv
import os

#Запуск polling, работает бесконечно
async def main():
    load_dotenv()
    bot = Bot(os.getenv('TOKEN'), parse_mode="HTML")
    dp = Dispatcher()
    dp.include_routers(heandlers.router, heandlers_schedule.router, handlers_none.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())