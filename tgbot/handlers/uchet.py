from aiogram import Dispatcher, types
from library.data import schet, pluss, minuss


async def suma(message: types.Message):
    text = f'{schet(message.from_user.id)} СОМ'
    await message.answer(text)


async def plus(message: types.Message):
    num = message.text.replace('/p', '').replace('/+', '').replace(' ', '')
    await message.answer(f'{pluss(num, message.from_user.id)} СОМ')


async def minus(message: types.Message):
    num = message.text.replace('/m', '').replace('/-', '').replace(' ', '')
    await message.answer(f'{minuss(num, message.from_user.id)} СОМ')


def register_uchet(dp: Dispatcher):
    dp.register_message_handler(suma, commands=['s'])
    dp.register_message_handler(plus, commands=['p', '+'])
    dp.register_message_handler(minus, commands=['m', '-'])
