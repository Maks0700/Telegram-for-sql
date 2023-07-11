""" import sqlite3 as sq
with sq.connect("DB.db") as con:
    cur = con.cursor()
    cur.execute("""""" CREATE TABLE IF NOT EXISTS photos(
                id INTEGER PRIMARY KEY,
                photo BLOB """

""" """   """)
    for i in range(1, 4):
        with open(f"{i}.jpg", "rb") as photo:
            h = photo.read()
            cur.execute("INSERT INTO photos(photo) VALUES(?)", [h]) """ """ """
import telebot
from telebot import types
import webbrowser
import sqlite3 as sq
bot = telebot.TeleBot("6218663006:AAGGboF-ByLwUBn0MUrTNv5kiYrAqzwGA34")


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Добро пожаловать!!")


@bot.message_handler(content_types=["text"])
def conv(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Имя", callback_data="name")
    btn2 = types.InlineKeyboardButton("ID", callback_data="id")
    markup.row(btn1, btn2)
    bot.reply_to(message, "Ты крутой чувак,выбери кнопку",
                 reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def call(callback):
    if callback.data == "name":
        bot.send_message("Hello", callback.message.chat.id,
                         callback.message.message_id)
    elif callback.data == "id":
        bot.send_message("Good", callback.message.chat.id,
                         callback.message.message_id)


bot.polling(non_stop=True)
