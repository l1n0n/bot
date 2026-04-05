import os
from random import *
from telebot import TeleBot, types
from dotenv import load_dotenv
from datetime import datetime
from zoneinfo import ZoneInfo
from timezonefinder import TimezoneFinder

load_dotenv()

t = TeleBot(os.getenv('BOT_TOKEN'))
tf = TimezoneFinder()

user_timezones = {}

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

@t.message_handler(content_types=['location'])
def handle_location(message):
    lat = message.location.latitude
    lng = message.location.longitude
    tz_name = tf.timezone_at(lng=lng, lat=lat)
    
    if tz_name:
        user_timezones[message.chat.id] = tz_name
        t.send_message(message.chat.id, f"Часовой пояс установлен: {tz_name}")
    else:
        t.send_message(message.chat.id, "Не удалось определить часовой пояс.")

@t.message_handler(commands=['schedule'])
def send_schedule(message):
    tz_name = user_timezones.get(message.chat.id, "UTC")
    now = datetime.now(ZoneInfo(tz_name))
    t.send_message(message.chat.id, schedule[now.weekday()])

@t.message_handler(commands=['date'])
def send_date(message):
    chat_id = message.chat.id
    if chat_id not in user_timezones:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        btn = types.KeyboardButton("Отправить локацию", request_location=True)
        markup.add(btn)
        t.send_message(chat_id, "Сначала отправь свою локацию, чтобы я узнал твой часовой пояс.", reply_markup=markup)
        return

    tz_name = user_timezones[chat_id]
    now = datetime.now(ZoneInfo(tz_name))
    
    weekdays = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    
    date_str = f"{weekdays[now.weekday()]}, {now.day} {months[now.month - 1]} {now.year} {now.strftime('%H:%M:%S')}"
    t.send_message(chat_id, date_str)

@t.message_handler(commands='rand')
def send_random(message):
    t.send_message(message.chat_id, f'Random number: {randint(1,10)}')

t.infinity_polling()