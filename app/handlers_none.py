from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message()
async def cmd_none(message: Message):
    await message.answer('Простите, я не знаю такой команды. Обратитесь к команде /help')