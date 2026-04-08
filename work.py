import os
from random import *
from telebot import TeleBot
from dotenv import load_dotenv
from datetime import datetime
from time import *

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

weekdays = 'Понедельник Вторник Среда Четверг Пятница Суббота Воскресенье'.split()

def toString(d: datetime):
    return f'''Сейчас в Иннополисе:
{weekdays[d.weekday()]}, {d.day}.{d.month}.{d.year}, {d.hour}:{d.minute}:{d.second}
''' 

CHANNEL = '@mvnntl_t_nthr_cntr'

def is_subscribed(user_id):
    try:
        member = t.get_chat_member(CHANNEL, user_id)
        print(f"User {user_id} status: {member.status}")
        return member.status in ['member', 'administrator', 'creator']
    except Exception as e:
        print(f"Error checking subscription: {e}")
        return False

def check_subscription(message):
    if not is_subscribed(message.from_user.id):
        t.send_message(message.chat.id, f'Для использования бота подпишитесь на канал: {CHANNEL}')
        return False
    return True

@t.message_handler(commands=['start'])
def start(message):
    t.send_message(message.chat.id, "Привет! Чтобы я показывал правильное время, пришли мне свою геопозицию (кнопку в меню), а затем используй /date или /schedule.")

@t.message_handler(commands=['schedule'])
def send_schedule(message):
    if not check_subscription(message):
        return
    old = (datetime.now() - datetime(1970, 1, 1, 0, 0, 0, 0)).total_seconds() + 10800
    new = datetime.fromtimestamp(old)
    t.send_message(message.chat.id, schedule[new.weekday()])

@t.message_handler(commands=['date'])
def send_date(message):
    if not check_subscription(message):
        return
    old = (datetime.now() - datetime(1970, 1, 1, 0, 0, 0, 0)).total_seconds() + 10800
    new = datetime.fromtimestamp(old)
    t.send_message(message.chat.id, toString(old))

t.infinity_polling()