from telebot import *

t = TeleBot('6015308173:AAEAnP8IYiwrayHSR8Hl2zuRgRalYYd9sn4')


@t.message_handler(commands=['start'])
def send_welcome(message):
    t.send_message(message.chat.id, "Привет! 👋")


t.infinity_polling()