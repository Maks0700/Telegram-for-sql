import telebot
from telebot import types
import webbrowser
import sqlite3 as sq
import requests
import  json

bot = telebot.TeleBot("6218663006:AAGGboF-ByLwUBn0MUrTNv5kiYrAqzwGA34")

key_api="936f1d577ed80415503d1a56fcdcedcf"
url="https://api.openweathermap.org/data/2.5/weather?q=London&appid=936f1d577ed80415503d1a56fcdcedcf&units=metric"
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,"Привет,рад тебя видеть!Напиши название города!")

@bot.message_handler(content_types=["text"])
def get_weather(message):
    city=message.text.lower().lstrip()
    res=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=936f1d577ed80415503d1a56fcdcedcf&units=metric")
    if res.status_code==200:
        data=json.loads(res.text)
        
        weather_new=data["weather"][0]["main"]
        
        #bot.send_message(message.chat.id,weather_new)
        if "rain" in weather_new.lower(): 
            weather_picture=open("Дождливо.gif","rb")
            bot.send_photo(message.chat.id,weather_picture)
        elif "clouds" in weather_new.lower():
            weather_picture=open("Пасмурно.jpg","rb")
            bot.send_photo(message.chat.id,weather_picture)
        weather_picture=None


    else:
        bot.reply_to(message,"Город указан неверно,введите снова город!!")

bot.polling(non_stop=True)
