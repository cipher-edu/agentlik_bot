from aiogram import types

from loader import dp
import wikipedia
wikipedia.set_lang('uz')
# Echo bot
# @dp.message_handler(state=None)
# async def bot_echo(message: types.Message):
#     await message.answer(message.text)
@dp.message_handler()
async def sendWiki(message: types.Message):
    print(message.chat.id)
    try:
        respond = wikipedia.summary(message.text)

    except:
        await message.answer("Bu mavzuga oid maqolani topa olmadim")