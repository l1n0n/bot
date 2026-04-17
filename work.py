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
from datetime import datetime, timedelta, timezone

# --- КОНФИГУРАЦИЯ ---
TELEGRAM_TOKEN = "6015308173:AAEAnP8IYiwrayHSR8Hl2zuRgRalYYd9sn4"
INNOHASSLE_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiI2OGE0MGVkNGFkOTkyYTk0YjBmYTM0NjQiLCJlbWFpbCI6Imwua2FzaW1vdkBpbm5vcG9saXMudW5pdmVyc2l0eSIsInRlbGVncmFtX2lkIjoxMjQ3NjgxNjc2LCJleHAiOjE3NzY1MzI2NjksImlhdCI6MTc3NjQ0NjI2OSwic2NvcGUiOiJtZSJ9.KdqD6Bh79do9vKsMnmlYQBfSCCv634yeDb08k8TmHZQgCf5ZKcaHLYYcxrIQtzMPIvPJPfSXUU-1qmNFumZl6XYJpTWncyJ79eeLD_Jc3SpY5J2OZAncQzBMTHw_vHVqtD6KICekMvpbKnqO9IRzMeo0chQrGVCgGvTfHARTa-t3pZO21bQf2JDB9EspyUjzkLSR1Bz_73tDyFr3OQaL-VRkPBlWvea27xuk40xvBHmvGGRki4MG7KPMYyaXFTPR41Aac_p48_D74EcPshpJEyql0d2I-F1NWmEp6zt-b3sa3I1EbyG0zS1EuBo0S5YVm4Sezesm0mLLnQBs3Tl_EA"
GROUP_ID = "65f1c243673c660600f723e7"

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def get_schedule():
    url = "https://api.innohassle.ru/events/v0/events/search/"
    headers = {
        "Authorization": f"Bearer {INNOHASSLE_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "filter": {"group_ids": [GROUP_ID]},
        "limit": 100
    }
    try:
        r = requests.post(url, json=payload, headers=headers, timeout=10)
        if r.status_code == 200:
            return r.json().get('items', []), None
        return None, f"Ошибка API: {r.status_code}\n{r.text[:100]}"
    except Exception as e:
        return None, f"Ошибка сети: {str(e)}"

@bot.message_handler(commands=['start', 'today'])
def send_today(message):
    data, error = get_schedule()
    
    if error:
        bot.reply_to(message, f"❌ {error}")
        return

    # Устанавливаем часовой пояс Иннополиса (UTC+3)
    tz_inno = timezone(timedelta(hours=3))
    today = datetime.now(tz_inno).date()
    
    res = []
    for event in data:
        # Парсим время из API
        dt_str = event['start_time'].replace('Z', '+00:00')
        dt_utc = datetime.fromisoformat(dt_str)
        # Переводим время в часовой пояс Иннополиса
        dt_local = dt_utc.astimezone(tz_inno)
        
        if dt_local.date() == today:
            time_start = dt_local.strftime('%H:%M')
            res.append(f"⏰ `{time_start}` — *{event.get('name', 'Занятие')}*\n📍 {event.get('location', 'Аудитория не указана')}")

    if not res:
        bot.send_message(message.chat.id, f"📅 На сегодня ({today.strftime('%d.%m')}) пар не найдено!")
    else:
        output = f"📅 *Расписание на сегодня ({today.strftime('%d.%m')}):*\n\n" + "\n\n".join(sorted(res))
        bot.send_message(message.chat.id, output, parse_mode="Markdown")

if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()