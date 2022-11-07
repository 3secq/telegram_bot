from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import api_key

import markups as kb


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nТы можешь использовать мои команды даже в Telegram боте!")



@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Из доступных команд могу выделить : узнать погоду, рассказать анекдот, запустить игру.", reply_markup=kb.inline_kb1)

if __name__ == '__main__':
    executor.start_polling(dp)