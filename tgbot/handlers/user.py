from aiogram import Dispatcher, types
from library.data import create_data, data


async def user_start(message: types.Message):
    about = data()
    print(about)
    print(message.from_user.id)
    if str(message.from_user.id) not in about:
        create_data(name=message.from_user.full_name, nick=f'@{message.from_user.username}', cash=0, telegram_id=message.from_user.id)
    await message.reply("Салам это бот для учета твоих денег\nДля роботы с ботом: /help")


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
