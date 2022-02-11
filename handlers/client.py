from aiogram import  types,Dispatcher
from create_bot import dp,bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db




# @dp.message_handler(commands=['start','help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита!',reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему: \nhttps://t.me/test080989_bot')


# @dp.message_handler(commands=['Режим_работы'])
async def work_time(message : types.Message):
    await bot.send_message(message.from_user.id, 'monday from 9am to 8pm')

# @dp.message_handler(commands=['Расположение'])
async def place(message: types.Message):
    await bot.send_message(message.from_user.id, 'Oybek street ',reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands=['меню'])
async def menu(message: types.Message):
    await sqlite_db.sql_read(message)

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start','help'])
    dp.register_message_handler(work_time, commands=['Режим_работы'])
    dp.register_message_handler(place, commands=['Расположение'])
    dp.register_message_handler(menu,commands=['меню'])
