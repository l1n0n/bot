import os
from telebot import TeleBot
from dotenv import load_dotenv

load_dotenv()

t = TeleBot(os.getenv('BOT_TOKEN'))


@t.message_handler(commands=['start'])
def send_woliday(message):
    t.send_message(message.chat.id, "Привет! 👋")


t.infinity_polling()