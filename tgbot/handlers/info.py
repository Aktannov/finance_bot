from aiogram import Dispatcher, types

from library.data import data


async def bot_info(message: types.Message):
    text = f'ID: {message.from_user.id}\nFull_name: {message.from_user.full_name}\nUser_name: @{message.from_user.username}\nLanguage: {message.from_user.language_code}'
    text2 = data()
    await message.answer(f'Ваше info ;)\n{text}\n{text2}')



def register_info(dp: Dispatcher):
    dp.register_message_handler(bot_info, commands='info')