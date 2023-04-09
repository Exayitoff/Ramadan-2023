import datetime
from tugma import keyboard, ramadan




import logging

from aiogram import Bot, Dispatcher, executor, types 
from aiogram.types import CallbackQuery
API_TOKEN = '6183890287:AAFNWNna62PNyP3ZBNvbJWxYP2-F715knDE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await bot.send_photo(chat_id=message.from_user.id, photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIt7RzsgB2Ee9tUfD4X_bvIIZZsy19eTNW0A&usqp=CAU', caption=f"Assalomu alaykum {message.from_user.first_name} \nUshbu bot orqali Xorazm Ramazon taqvimini bilib bolishingiz mumkin!  🕋 ", reply_markup=keyboard)



@dp.callback_query_handler(lambda c: c.data == 'kecha')
async def kecha(callback_query: CallbackQuery):
    x = datetime.datetime.now()
    day = x.strftime("%d")
    last_day = int(day)-1
    for i in ramadan:
        if int(i['kun']) == last_day:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo="https://marketplace.canva.com/EAFc8T7klhI/1/0/1600w/canva-green-modern-ramadan-mubarak-free-instagram-post-P0hRqLvxKA8.jpg", caption=f"<b>Kechagi ramazon taqvimi</b>\n🌅Saharlik vaqti: <b>{i['Saharlik']}</b>\n🌃Iftorlik vaqti: <b>{i['Iftorlik']}</b>\n<b>Kechagi sana: {i['kun']}-aprel</b>", parse_mode="HTML" , reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data == 'bugun')
async def kecha(callback_query: CallbackQuery):
    x = datetime.datetime.now()
    day = x.strftime("%d")
    last_day = int(day)
    for i in ramadan:
        if int(i['kun']) == last_day:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo="https://marketplace.canva.com/EAFc8T7klhI/1/0/1600w/canva-green-modern-ramadan-mubarak-free-instagram-post-P0hRqLvxKA8.jpg", caption=f"<b>Bugungi ramazon taqvimi</b>\n🌅Saharlik vaqti: <b>{i['Saharlik']}</b>\n🌃Iftorlik vaqti: <b>{i['Iftorlik']}</b>\n<b>Bugungi sana: {i['kun']}-aprel</b>", parse_mode="HTML" , reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data == 'ertaga')
async def kecha(callback_query: CallbackQuery):
    x = datetime.datetime.now()
    day = x.strftime("%d")
    last_day = int(day)+1
    for i in ramadan:
        if int(i['kun']) == last_day:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo="https://marketplace.canva.com/EAFc8T7klhI/1/0/1600w/canva-green-modern-ramadan-mubarak-free-instagram-post-P0hRqLvxKA8.jpg", caption=f"<b>Ertangi ramazon taqvimi</b>\n🌅Saharlik vaqti: <b>{i['Saharlik']}</b>\n🌃Iftorlik vaqti: <b>{i['Iftorlik']}</b>\n<b>Ertangi sana: {i['kun']}-aprel</b>", parse_mode="HTML" , reply_markup=keyboard)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)