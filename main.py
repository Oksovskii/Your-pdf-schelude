import requests
import telebot
import func as f
import const as c
from datetime import datetime

#Token of your bot
bot = telebot.TeleBot(c.token)

bot.send_message(681875938, 'Im started at {%s} (UTC+0)' %
                 str(datetime.strftime(datetime.now(), "%H:%M:%S")))


@bot.message_handler(commands=['start'])
def send_welcome(message):
    msg = bot.send_message(
        message.chat.id, 'Привет! Я присылаю расписание для "ВКСиИТ"!\n Напиши {/help} для подробной информации.')


@bot.message_handler(commands=['help'])
def send_message(message):
    msg = bot.send_message(
        message.chat.id, 'Использование: {/rasp} - запрос расписания НПО.')


@bot.message_handler(commands=['rasp'])
def send_photo(message):
    f.schelude()
    msg = bot.send_message(message.chat.id, 'Расписание:>')
    bot.send_photo(message.chat.id, photo=open('img/rasp-1.jpg', 'rb'))


bot.polling()