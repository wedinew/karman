import bot_main as ss
from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import random
import pars

content=pars.films()
print(content)
# Объект бота
bot = Bot(token="1974008031:AAHQraVsEdg0tmOENNusIs1vDESg53oV_58")
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения



# Хэндлер на команду /test1
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Начинаем!",reply_markup=ss.main)
@dp.message_handler()


async def process_start_command(message: types.Message):
    if message.text =="Посоветовать фильм":
        await message.reply("посоветовать фильм", reply_markup=ss.film_menu)
    if message.text =="Рандомно🎲":
        rand_janr=random.choice(['боевик','комедия','вестерн','детектив','детский','фэнтези'])
        rand_film=random.randint(0,len(content[rand_janr]['film_name'])-1)
        photo = open(content[rand_janr]['film_name'][rand_film]+'.jpg', 'rb')
        await bot.send_photo(chat_id=message.chat.id, photo=photo,caption=
                            content[rand_janr]['film_name'][rand_film].replace(')','»').replace('(','«').replace(';',':').replace("?","+").replace(')','"').replace('99','/')
                            +'\n'
                            +content[rand_janr]['film_janr'][rand_film]+'\n'
                            +content[rand_janr]['film_year'][rand_film])

    if message.text=="Боевики👊":
        janr="боевик"
        rand_film=random.randint(0,len(content["боевик"]['film_name'])-1)
        photo = open(content["боевик"]['film_name'][rand_film]+'.jpg', 'rb')
        await bot.send_photo(chat_id=message.chat.id, photo=photo,caption=
                            content["боевик"]['film_name'][rand_film].replace(')','»').replace('(','«').replace(';',':').replace("?","+").replace(')','"').replace('99','/')
                            +'\n'
                            +content["боевик"]['film_janr'][rand_film]+'\n'
                            +content["боевик"]['film_year'][rand_film])
    if message.text=="Комедии💃":
        janr="комедия"
        rand_film=random.randint(0,len(content['комедия']['film_name'])-1)
        photo = open(content['комедия']['film_name'][rand_film]+'.jpg', 'rb')
        await bot.send_photo(chat_id=message.chat.id, photo=photo,caption=
                            content['комедия']['film_name'][rand_film].replace(')','»').replace('(','«').replace(';',':').replace("?","+").replace(')','"').replace('99','/')
                            +'\n'
                            +content['комедия']['film_janr'][rand_film]+'\n'
                            +content['комедия']['film_year'][rand_film])
    if message.text=="Вестерны🎩":
        janr="вестерн"
        rand_film=random.randint(0,len(content["вестерн"]['film_name'])-1)
        photo = open(content["вестерн"]['film_name'][rand_film]+'.jpg', 'rb')
        await bot.send_photo(chat_id=message.chat.id, photo=photo,caption=
                            content["вестерн"]['film_name'][rand_film].replace(')','»').replace('(','«').replace(';',':').replace("?","+").replace(')','"').replace('99','/')
                            +'\n'
                            +content["вестерн"]['film_janr'][rand_film]+'\n'
                            +content["вестерн"]['film_year'][rand_film])
    if message.text=="Детективы🔎":
            janr='детектив'
            rand_film=random.randint(0,len(content['детектив']['film_name'])-1)
            photo = open(content['детектив']['film_name'][rand_film]+'.jpg', 'rb')
            await bot.send_photo(chat_id=message.chat.id, photo=photo,caption=
                                content['детектив']['film_name'][rand_film].replace(')','»').replace('(','«').replace(';',':').replace("?","+").replace(')','"').replace('99','/')
                                +'\n'
                                +content['детектив']['film_janr'][rand_film]+'\n'
                                +content['детектив']['film_year'][rand_film])
    if message.text=="Детские👶":
        janr='детский'
        rand_film=random.randint(0,len(content['детский']['film_name'])-1)
        photo = open(content['детский']['film_name'][rand_film]+'.jpg', 'rb')
        await bot.send_photo(chat_id=message.chat.id, photo=photo,caption=
                            content['детский']['film_name'][rand_film].replace(')','»').replace('(','«').replace(';',':').replace("?","+").replace(')','"').replace('99','/')
                            +'\n'
                            +content['детский']['film_janr'][rand_film]+'\n'
                            +content['детский']['film_year'][rand_film])
    if message.text=="Фэнтази👾":
            janr='фэнтези'
            rand_film=random.randint(0,len(content['фэнтези']['film_name'])-1)
            photo = open(content['фэнтези']['film_name'][rand_film]+'.jpg', 'rb')
            await bot.send_photo(chat_id=message.chat.id, photo=photo,caption=
                                content['фэнтези']['film_name'][rand_film].replace(')','»').replace('(','«').replace(';',':').replace("?","+").replace(')','"').replace('99','/')
                                +'\n'
                                +content['фэнтези']['film_janr'][rand_film]+'\n'
                                +content['фэнтези']['film_year'][rand_film])


    #________________________mebu random____________________#
    if message.text =="Рандомное число":
        await message.answer("рандомное число", reply_markup=ss.main2)
    if message.text == "От 1 до 10":
        await message.answer(random.randint(1,10))
    if message.text == "От 1 до 100":
        await message.answer(random.randint(1,100))
    if message.text == "От 1 до 1000":
        await message.answer(random.randint(1,1000))
    if message.text =="В меню":
        await message.reply("Начинаем заново!",reply_markup=ss.main)
     #________________________________________________________#

executor.start_polling(dp, skip_updates=True)
