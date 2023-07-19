import telebot
from telebot import types
import webbrowser
import sqlite3 as sq
import requests
import json

bot = telebot.TeleBot("6218663006:AAGGboF-ByLwUBn0MUrTNv5kiYrAqzwGA34")
city = " "
key_api = "936f1d577ed80415503d1a56fcdcedcf"
url = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=936f1d577ed80415503d1a56fcdcedcf&units=metric"
with sq.connect("DB for tg bot weather.db") as conn:
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS status_weather(
                temperature INTEGER NOT NULL,
                main_weather TEXT NOT NULL

    )""")


@bot.message_handler(commands=["start"])
def start(message):

    bot.send_message(
        message.chat.id, "Привет,рад тебя видеть!Напиши название города!")
    city = message.text.lower().lstrip()


@bot.message_handler(content_types=["text"])
def but(message):

    markup = types.ReplyKeyboardMarkup()
    temp = types.KeyboardButton("Температура воздуха в городе")
    main_weather = types.KeyboardButton("Погода в городе")
    markup.add(temp, main_weather)
    bot.send_message(message.chat.id, "Что тебя интересует?",
                     reply_markup=markup)


@bot.message_handler(content_types=["text"])
def on_click(message):
    global city
    if message.text.lower() == "Погода в городе":
        res = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=936f1d577ed80415503d1a56fcdcedcf&units=metric")
        data = json.loads(res.text)
        temper = data['main']['temp']
        context_clouds = data['weather'][0]['main']
        if "cloud" in context_clouds.lower():
            cloud_picture = open("Пасмурно.jpg", "rb")
            bot.send_photo(message.chat.id, cloud_picture)
            cur.execute(
                """INSERT INTO status_weather(main_weather) VALUES(?)""", context_clouds)
        elif "rain" in context_clouds.lower():
            cloud_picture = open("Дождливо.gif", "rb")
            bot.send_photo(message.chat.id, cloud_picture)
            cur.execute(
                """INSERT INTO status_weather(main_weather) VALUES(?)""", context_clouds)
    elif message.text == "Температура воздуха в городе":
        bot.send_message(
            message.chat.id, f"Сейчас температура в {city} {temper} градусов")
        cur.execute("""INSERT INTO status_weather(temperature) VALUES(?)""",
                    temper)


bot.polling(non_stop=True)
