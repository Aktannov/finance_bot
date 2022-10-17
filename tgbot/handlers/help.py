from aiogram import Dispatcher, types

async def bot_help(message: types.Message):
    text = 'Добавить деньги - /p сумма\nОтнять деньги - /m сумма\nОбщая сумма - /s'
    await message.answer(text)

def register_help(dp: Dispatcher):
    dp.register_message_handler(bot_help, commands='help')