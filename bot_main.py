from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

        #______________________menu_______________________#
film = KeyboardButton("Посоветовать фильм")
random = KeyboardButton("Рандомное число")
main = ReplyKeyboardMarkup().add(random,film)
menu=KeyboardButton("В меню")
        #_________________________________________________#
        #________________________random___________________#

rand_butt = KeyboardButton("От 1 до 10")
rand_butt2 = KeyboardButton("От 1 до 100")
rand_butt3 = KeyboardButton("От 1 до 1000")
menu=KeyboardButton("В меню")
main2 = ReplyKeyboardMarkup().add(rand_butt,rand_butt2,rand_butt3,menu)
    #____________________________________________________#

film1 = KeyboardButton("Комедии💃")
film2 = KeyboardButton("Боевики👊")
film3 = KeyboardButton("Вестерны🎩")
film4 = KeyboardButton("Детективы🔎")
film5 = KeyboardButton("Детские👶")

film7 = KeyboardButton("Фэнтази👾")
film8 = KeyboardButton("Рандомно🎲")
film_menu = ReplyKeyboardMarkup().add(film1,film2,film3,film4,film5,film7,film8,menu)
