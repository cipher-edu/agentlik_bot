import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

TOKEN = '5304967823:AAGUWKnofSfuEeQ7D3Hm6voK1O9bTWh_Y3s'
CHANNEL_ID = '1513797200'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Bot ishga tushdi!')

@dp.message_handler(commands=['check_user'])
async def check_user_command(message: types.Message):
    user_id = message.from_user.id
    channel_member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
    
    if channel_member.status in ['member', 'creator']:
        reply_message = 'Foydalanuvchi kanalda mavjud.'
    else:
        reply_message = 'Foydalanuvchi kanalda mavjud emas.'
    
    await message.reply(reply_message)

@dp.message_handler()
async def unknown_command(message: types.Message):
    await message.reply("Unknown command. Type /start to start the bot.")

# Start the bot
async def start_bot():
    await dp.start_polling()

if __name__ == '__main__':
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        pass
    finally:
        asyncio.run(dp.storage.close())
        asyncio.run(dp.storage.wait_closed())
