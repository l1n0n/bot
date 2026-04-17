# import os
# from random import *
# from telebot import TeleBot
# from dotenv import load_dotenv
# from datetime import datetime
# from time import *

# load_dotenv()
# t = TeleBot(os.getenv('BOT_TOKEN'))


# class Monday:
#     schedule = [{'start': {'hours': '09', 'minutes': '00'}, 'end': {'hours': '10', 'minutes': '30'}, 'name': 'DSA Lecture'},
#                 {'start': {'hours': '10', 'minutes': '40'}, 'end': {'hours': '12', 'minutes': '10'}, 'name': 'DSA Tutorial'},
#                 {'start': {'hours': '12', 'minutes': '40'}, 'end': {'hours': '14', 'minutes': '10'}, 'name': 'DSA Lab'},
#                 {'start': {'hours': '16', 'minutes': '00'}, 'end': {'hours': '17', 'minutes': '30'}, 'name': 'AWA'}
#                 ]
#     def __init__(self):
#         pass

#     @staticmethod
#     def lessonToString(lesson):
#         return f"{lesson['start']['hours']}:{lesson['start']['minutes']}-{lesson['end']['hours']}:{lesson['end']['minutes']}: {lesson['name']}"

#     def show_schedule(self, current):
#         res = ''
#         dayIsOver = True
#         for lesson in self.schedule:
#             if int(lesson['end']['hours']) * 3600 + int(lesson['end']['minutes']) * 60 <= current.hour * 3600 + current.minute * 60 + current.second:
#                 res = res + '✅' + Monday.lessonToString(lesson) + '\n'
#             elif int(lesson['start']['hours']) * 3600 + int(lesson['start']['minutes']) * 60 <= current.hour * 3600 + current.minute * 60 + current.second < int(lesson['end']['hours']) * 3600 + int(lesson['end']['minutes']) * 60:
#                 res = res + '🧑‍💻' + Monday.lessonToString(lesson) + '\n'
#                 dayIsOver = False
#             else:
#                 res = res + '❌' + Monday.lessonToString(lesson) + '\n'
#                 dayIsOver = False
#         return res + '\nНа сегодня занятия закончились! 🥳' if dayIsOver else res
    

# class Tuesday:
#     schedule = [{'start': {'hours': '09', 'minutes': '00'}, 'end': {'hours': '10', 'minutes': '30'}, 'name': 'SSAD Lecture'},
#                 {'start': {'hours': '10', 'minutes': '40'}, 'end': {'hours': '12', 'minutes': '10'}, 'name': 'SSAD Tutorial'},
#                 {'start': {'hours': '14', 'minutes': '20'}, 'end': {'hours': '15', 'minutes': '50'}, 'name': 'SSAD Lab'},
#                 {'start': {'hours': '16', 'minutes': '30'}, 'end': {'hours': '18', 'minutes': '00'}, 'name': 'Table Tennis Training'}
#                 ]
#     def __init__(self):
#         pass

#     @staticmethod
#     def lessonToString(lesson):
#         return f"{lesson['start']['hours']}:{lesson['start']['minutes']}-{lesson['end']['hours']}:{lesson['end']['minutes']}: {lesson['name']}"

#     def show_schedule(self, current):
#         res = ''
#         dayIsOver = True
#         for lesson in self.schedule:
#             if int(lesson['end']['hours']) * 3600 + int(lesson['end']['minutes']) * 60 <= current.hour * 3600 + current.minute * 60 + current.second:
#                 res = res + '✅' + Tuesday.lessonToString(lesson) + '\n'
#             elif int(lesson['start']['hours']) * 3600 + int(lesson['start']['minutes']) * 60 <= current.hour * 3600 + current.minute * 60 + current.second < int(lesson['end']['hours']) * 3600 + int(lesson['end']['minutes']) * 60:
#                 if 'Tennis' not in lesson['name']:
#                     res = res + '🧑‍💻' + Tuesday.lessonToString(lesson) + '\n'
#                 else:
#                     res = res + '🏓' + Tuesday.lessonToString(lesson) + '\n'
#                 dayIsOver = False
#             else:
#                 res = res + '❌' + Tuesday.lessonToString(lesson) + '\n'
#                 dayIsOver = False
#         return res + '\nНа сегодня занятия закончились! 🥳' if dayIsOver else res


# class Wednesday:
#     schedule = [{'start': {'hours': '09', 'minutes': '00'}, 'end': {'hours': '10', 'minutes': '30'}, 'name': 'Math Analysis Lecture'},
#                 {'start': {'hours': '10', 'minutes': '40'}, 'end': {'hours': '12', 'minutes': '10'}, 'name': 'Math Analysis Tutorial'},
#                 {'start': {'hours': '12', 'minutes': '40'}, 'end': {'hours': '14', 'minutes': '10'}, 'name': 'Math Analysis Lab'},
#                 {'start': {'hours': '16', 'minutes': '00'}, 'end': {'hours': '17', 'minutes': '30'}, 'name': 'AWA'}
#                 ]
#     def __init__(self):
#         pass

#     @staticmethod
#     def lessonToString(lesson: dict) -> str:
#         return f"{lesson['start']['hours']}:{lesson['start']['minutes']}-{lesson['end']['hours']}:{lesson['end']['minutes']}: {lesson['name']}"

#     def show_schedule(self, current) -> str:
#         res = ''
#         dayIsOver = True
#         for lesson in self.schedule:
#             if int(lesson['end']['hours']) * 3600 + int(lesson['end']['minutes']) * 60 <= current.hour * 3600 + current.minute * 60 + current.second:
#                 res = res + '✅' + Wednesday.lessonToString(lesson) + '\n'
#             elif int(lesson['start']['hours']) * 3600 + int(lesson['start']['minutes']) * 60 <= current.hour * 3600 + current.minute * 60 + current.second < int(lesson['end']['hours']) * 3600 + int(lesson['end']['minutes']) * 60:
#                 res = res + '🧑‍💻' + Wednesday.lessonToString(lesson) + '\n'
#                 dayIsOver = False
#             else:
#                 res = res + '❌' + Wednesday.lessonToString(lesson) + '\n'
#                 dayIsOver = False
#         return res + '\nНа сегодня занятия закончились! 🥳' if dayIsOver else res
    

# class Thursday:
#     schedule = [{'start': {'hours': '09', 'minutes': '00'}, 'end': {'hours': '10', 'minutes': '30'}, 'name': 'TCS Lecture'},
#                 {'start': {'hours': '10', 'minutes': '40'}, 'end': {'hours': '12', 'minutes': '10'}, 'name': 'TCS Tutorial'},
#                 {'start': {'hours': '12', 'minutes': '40'}, 'end': {'hours': '14', 'minutes': '10'}, 'name': 'TCS Lab'},
#                 {'start': {'hours': '16', 'minutes': '30'}, 'end': {'hours': '18', 'minutes': '00'}, 'name': 'Table Tennis Training'}
#                 ]
#     def __init__(self):
#         pass

#     @staticmethod
#     def lessonToString(lesson) -> str:
#         return f"{lesson['start']['hours']}:{lesson['start']['minutes']}-{lesson['end']['hours']}:{lesson['end']['minutes']}: {lesson['name']}"

#     def show_schedule(self, current):
#         res = ''
#         dayIsOver = True
#         for lesson in self.schedule:
#             if int(lesson['end']['hours']) * 3600 + int(lesson['end']['minutes']) * 60 <= current.hour * 3600 + current.minute * 60 + current.second:
#                 res = res + '✅' + Thursday.lessonToString(lesson) + '\n'
#             elif int(lesson['start']['hours']) * 3600 + int(lesson['start']['minutes']) * 60 <= current.hour * 3600 + current.minute * 60 + current.second < int(lesson['end']['hours']) * 3600 + int(lesson['end']['minutes']) * 60:
#                 if 'Tennis' not in lesson['name']:
#                     res = res + '🧑‍💻' + Thursday.lessonToString(lesson) + '\n'
#                 else:
#                     res = res + '🏓' + Thursday.lessonToString(lesson) + '\n'
#                 dayIsOver = False
#             else:
#                 res = res + '❌' + Thursday.lessonToString(lesson) + '\n'
#                 dayIsOver = False
#         return res + '\nНа сегодня занятия закончились! 🥳' if dayIsOver else res
    

# class Friday:
#     schedule = [{'start': {'hours': '09', 'minutes': '00'}, 'end': {'hours': '10', 'minutes': '30'}, 'name': 'AGLA Lecture'},
#                 {'start': {'hours': '10', 'minutes': '40'}, 'end': {'hours': '12', 'minutes': '10'}, 'name': 'AGLA Tutorial'},
#                 {'start': {'hours': '12', 'minutes': '40'}, 'end': {'hours': '14', 'minutes': '10'}, 'name': 'AGLA Lab'}
#                 ]
#     def __init__(self):
#         pass

#     @staticmethod
#     def lessonToString(lesson):
#         return f"{lesson['start']['hours']}:{lesson['start']['minutes']}-{lesson['end']['hours']}:{lesson['end']['minutes']}: {lesson['name']}"

#     def show_schedule(self, current):
#         res = ''
#         dayIsOver = True
#         for lesson in self.schedule:
#             if int(lesson['end']['hours']) * 3600 + int(lesson['end']['minutes']) * 60 <= current.hour * 3600 + current.minute * 60 + current.second:
#                 res = res + '✅' + Friday.lessonToString(lesson) + '\n'
#             elif int(lesson['start']['hours']) * 3600 + int(lesson['start']['minutes']) * 60 <= current.hour * 3600 + current.minute * 60 + current.second < int(lesson['end']['hours']) * 3600 + int(lesson['end']['minutes']) * 60:
#                 res = res + '🧑‍💻' + Friday.lessonToString(lesson) + '\n'
#                 dayIsOver = False
#             else:
#                 res = res + '❌' + Friday.lessonToString(lesson) + '\n'
#                 dayIsOver = False
#         return res + '\nНа сегодня занятия закончились! 🥳' if dayIsOver else res
    

# class Saturday:
#     def __init__(self):
#         pass

#     def show_schedule(self, d: datetime):
#         return 'Сегодня ничего нет'
    

# class Sunday:
#     schedule = [{'start': {'hours': '11', 'minutes': '30'}, 'end': {'hours': '13', 'minutes': '00'}, 'name': 'Table Tennis Tournament'},]
#     def __init__(self):
#         pass

#     @staticmethod
#     def lessonToString(lesson):
#         return f"{lesson['start']['hours']}:{lesson['start']['minutes']}-{lesson['end']['hours']}:{lesson['end']['minutes']}: {lesson['name']}"

#     def show_schedule(self, current):
#         res = ''
#         dayIsOver = True
#         for lesson in self.schedule:
#             if int(lesson['end']['hours']) * 3600 + int(lesson['end']['minutes']) * 60 <= current.hour * 3600 + current.minute * 60 + current.second:
#                 res = res + '✅' + Sunday.lessonToString(lesson) + '\n'
#             elif int(lesson['start']['hours']) * 3600 + int(lesson['start']['minutes']) * 60 <= current.hour * 3600 + current.minute * 60 + current.second < int(lesson['end']['hours']) * 3600 + int(lesson['end']['minutes']) * 60:
#                 res = res + '🏓' + Sunday.lessonToString(lesson) + '\n'
#                 dayIsOver = False
#             else:
#                 res = res + '❌' + Sunday.lessonToString(lesson) + '\n'
#                 dayIsOver = False
#         return res + '\nНа сегодня занятия закончились! 🥳' if dayIsOver else res

# days = {
#     0: Monday(),
#     1: Tuesday(),
#     2: Wednesday(),
#     3: Thursday(),
#     4: Friday(),
#     5: Saturday(),
#     6: Sunday()
# }


# weekdays = 'Понедельник Вторник Среда Четверг Пятница Суббота Воскресенье'.split()

# def toString(d: datetime):
#     return f'''Сейчас в Иннополисе:\n{weekdays[d.weekday()]}, {d.day:02d}.{d.month:02d}.{d.year}, {d.hour:02d}:{d.minute:02d}:{d.second:02d}''' 

# CHANNEL = '@mvnntl_t_nthr_cntr'

# def is_subscribed(user_id):
#     try:
#         member = t.get_chat_member(CHANNEL, user_id)
#         print(f"User {user_id} status: {member.status}")
#         return member.status in ['member', 'administrator', 'creator']
#     except Exception as e:
#         print(f"Error checking subscription: {e}")
#         return False

# def check_subscription(message):
#     if not is_subscribed(message.from_user.id):
#         t.send_message(message.chat.id, f'Для использования бота подпишитесь на канал: {CHANNEL}')
#         return False
#     return True

# def getCorrectDate():
#     old = (datetime.now() - datetime(1970, 1, 1, 0, 0, 0, 0)).total_seconds() + 10800
#     new = datetime.fromtimestamp(old)
#     return new

# @t.message_handler(commands=['start'])
# def start(message):
#     t.send_message(message.chat.id, "Привет! Я бот, который может показывать сегодняшнее расписание лекций в Университете Иннополис.\n\nЧтобы узнать сегодняшнюю дату, нажмите сюда: /date\n\nЧтобы узнать сегодняшнее расписание, нажмите сюда: /schedule")

# @t.message_handler(commands=['schedule'])
# def send_schedule(message):
#     if not check_subscription(message):
#         return
#     correct = getCorrectDate()
#     t.send_message(message.chat.id, days[correct.weekday()].show_schedule(correct))

# @t.message_handler(commands=['date'])
# def send_date(message):
#     if not check_subscription(message):
#         return
#     t.send_message(message.chat.id, toString(getCorrectDate()))

# t.infinity_polling()

import telebot
import requests
from datetime import datetime

# --- ДАННЫЕ ДЛЯ РАБОТЫ ---
TELEGRAM_TOKEN = "6015308173:AAEAnP8IYiwrayHSR8Hl2zuRgRalYYd9sn4"
INNOHASSLE_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo2NTExNywiZW1haWwiOiJsLmthc2ltb3ZAYW5ub3BvbGlzLnVuaSIsImdyb3VwIjoiQjI1LTAxIn0.something_secret" 
GROUP_ID = "65f1c243673c660600f723e7"

API_URL = "https://api.innohassle.ru/events/v0/events/search/"

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def get_schedule():
    headers = {
        "Authorization": f"Bearer {INNOHASSLE_TOKEN}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "filter": {
            "group_ids": [GROUP_ID]
        },
        "limit": 100
    }

    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json().get('items', [])
        return None
    except:
        return None

def format_schedule(events):
    if not events:
        return "❌ Ошибка получения данных или расписание пусто."

    today = datetime.now().date()
    today_events = []

    for event in events:
        # Убираем 'Z' и парсим время
        time_str = event['start_time'].replace('Z', '+00:00')
        start_dt = datetime.fromisoformat(time_str)
        
        if start_dt.date() == today:
            today_events.append({
                "time": start_dt.strftime("%H:%M"),
                "name": event.get('name', 'Занятие'),
                "room": event.get('location', 'Аудитория не указана')
            })

    if not today_events:
        return "📅 На сегодня пар не найдено. Отдыхай!"

    today_events.sort(key=lambda x: x['time'])

    msg = f"📅 *Расписание на сегодня ({today.strftime('%d.%m')}):*\n\n"
    for ev in today_events:
        msg += f"⏰ `{ev['time']}` — *{ev['name']}*\n📍 {ev['room']}\n\n"
    
    return msg

@bot.message_handler(commands=['start', 'today'])
def send_today(message):
    bot.send_chat_action(message.chat.id, 'typing')
    events = get_schedule()
    text = format_schedule(events)
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

if __name__ == "__main__":
    print("Бот запущен и готов к работе!")
    bot.infinity_polling()