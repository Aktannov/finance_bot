from aiogram import Dispatcher, types

from library.data import schet


async def suma(message: types.Message):

    text = f'{schet(message.from_user.id)} СОМ'
    await message.answer(text)


def register_uchet(dp: Dispatcher):
    dp.register_message_handler(suma, commands=['sum'])

