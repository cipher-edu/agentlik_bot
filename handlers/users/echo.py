from aiogram import types
import responses
from loader import dp
import wikipedia
wikipedia.set_lang('uz')


@dp.message_handler()
async def sendWiki(message: types.Message):
    print(message.chat.id)
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)

    except:
        await message.answer("Bu mavzuga oid malumot yoq")
# # Echo bot
# @dp.message_handler(state=None)
# async def bot_echo(message: types.Message):
#     await message.answer(message.text)
