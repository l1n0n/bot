import os
from random import *
from telebot import TeleBot, types
from dotenv import load_dotenv
from datetime import datetime
from zoneinfo import ZoneInfo
from timezonefinder import TimezoneFinder

load_dotenv()

t = TeleBot(os.getenv('BOT_TOKEN'))

schedule = [
    '09:00-10:30 DSA Lecture\n10:40-12:10 DSA Tutorial\n12:40-14:10 DSA Lab\n16:00-17:30: AWA',
    '09:00-10:30 SSAD Lecture\n10:40-12:10 SSAD Tutorial\n14:20-15:50 SSAD Lab\n16:30-18:00: Table Tennis Training',
    '09:00-10:30 Math Analysis Lecture\n10:40-12:10 Math Analysis Tutorial\n12:40-14:10 Math Analysis Lab\n16:00-17:30: AWA',
    '09:00-10:30 TCS Lecture\n10:40-12:10 TCS Tutorial\n12:40-14:10 TCS Lab\n16:30-18:00: Table Tennis Training',
    '09:00-10:30 AGLA Lecture\n10:40-12:10 AGLA Tutorial\n12:40-14:10 AGLA Lab',
    '10:40-14:10 Software Engineering Toolkit',
    '11:30-13:00 Table Tennis Tournament'
]

@t.message_handler(commands=['start'])
def start(message):
    t.send_message(message.chat.id, "Привет! Чтобы я показывал правильное время, пришли мне свою геопозицию (кнопка в меню), а затем используй /date или /schedule.")

@t.message_handler(commands=['schedule'])
def send_schedule(message):
    t.send_message(message.chat.id, schedule[datetime.now().weekday()])

t.infinity_polling()