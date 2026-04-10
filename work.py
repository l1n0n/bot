import os
from random import *
from telebot import TeleBot
from dotenv import load_dotenv
from datetime import datetime
from time import *

load_dotenv()
t = TeleBot(os.getenv('BOT_TOKEN'))


class Monday:
    schedule = [{'start': {'hours': '09', 'minutes': '00'}, 'end': {'hours': '10', 'minutes': '30'}, 'name': 'DSA Lecture'},
                {'start': {'hours': '10', 'minutes': '40'}, 'end': {'hours': '12', 'minutes': '10'}, 'name': 'DSA Tutorial'},
                {'start': {'hours': '12', 'minutes': '40'}, 'end': {'hours': '14', 'minutes': '10'}, 'name': 'DSA Lab'},
                {'start': {'hours': '16', 'minutes': '00'}, 'end': {'hours': '17', 'minutes': '30'}, 'name': 'AWA'}
                ]
    def __init__(self):
        pass

    @staticmethod
    def lessonToString(lesson):
        return f"{lesson['start']['hours']}:{lesson['start']['minutes']}-{lesson['end']['hours']}:{lesson['end']['minutes']}: {lesson['name']}"

    def show_schedule(self):
        res = ''
        current = getCorrectDate()
        for lesson in self.schedule:
            if int(lesson['end']['hours']) * 3600 + int(lesson['end']['minutes']) * 60 > current.hour * 3600 + current.minutes * 60 + current.second:
                res = res + '✅' + Monday.lessonToString(lesson) + '\n'
            else:
                res = res + '❌' + Monday.lessonToString(lesson) + '\n'
        return res
    

class Tuesday:
    schedule = [{'start': {'hours': '09', 'minutes': '00'}, 'end': {'hours': '10', 'minutes': '30'}, 'name': 'SSAD Lecture'},
                {'start': {'hours': '10', 'minutes': '40'}, 'end': {'hours': '12', 'minutes': '10'}, 'name': 'SSAD Tutorial'},
                {'start': {'hours': '14', 'minutes': '20'}, 'end': {'hours': '15', 'minutes': '50'}, 'name': 'SSAD Lab'},
                {'start': {'hours': '16', 'minutes': '30'}, 'end': {'hours': '18', 'minutes': '00'}, 'name': 'Table Tennis Training'}
                ]
    def __init__(self):
        pass

    @staticmethod
    def lessonToString(lesson):
        return f"{lesson['start']['hours']}:{lesson['start']['minutes']}-{lesson['end']['hours']}:{lesson['end']['minutes']}: {lesson['name']}"

    def show_schedule(self):
        res = ''
        current = getCorrectDate()
        for lesson in self.schedule:
            if int(lesson['end']['hours']) * 3600 + int(lesson['end']['minutes']) * 60 > current.hour * 3600 + current.minutes * 60 + current.second:
                res = res + '✅' + Tuesday.lessonToString(lesson) + '\n'
            else:
                res = res + '❌' + Tuesday.lessonToString(lesson) + '\n'
        return res


class Wednesday:
    schedule = [{'start': {'hours': '09', 'minutes': '00'}, 'end': {'hours': '10', 'minutes': '30'}, 'name': 'Math Analysis Lecture'},
                {'start': {'hours': '10', 'minutes': '40'}, 'end': {'hours': '12', 'minutes': '10'}, 'name': 'Math Analysis Tutorial'},
                {'start': {'hours': '12', 'minutes': '40'}, 'end': {'hours': '14', 'minutes': '10'}, 'name': 'Math Analysis Lab'},
                {'start': {'hours': '16', 'minutes': '00'}, 'end': {'hours': '17', 'minutes': '30'}, 'name': 'AWA'}
                ]
    def __init__(self):
        pass

    @staticmethod
    def lessonToString(lesson):
        return f"{lesson['start']['hours']}:{lesson['start']['minutes']}-{lesson['end']['hours']}:{lesson['end']['minutes']}: {lesson['name']}"

    def show_schedule(self):
        res = ''
        current = getCorrectDate()
        for lesson in self.schedule:
            if int(lesson['end']['hours']) * 3600 + int(lesson['end']['minutes']) * 60 > current.hour * 3600 + current.minutes * 60 + current.second:
                res = res + '✅' + Wednesday.lessonToString(lesson) + '\n'
            else:
                res = res + '❌' + Wednesday.lessonToString(lesson) + '\n'
        return res
    

class Thursday:
    schedule = [{'start': {'hours': '09', 'minutes': '00'}, 'end': {'hours': '10', 'minutes': '30'}, 'name': 'TCS Lecture'},
                {'start': {'hours': '10', 'minutes': '40'}, 'end': {'hours': '12', 'minutes': '10'}, 'name': 'TCS Tutorial'},
                {'start': {'hours': '12', 'minutes': '40'}, 'end': {'hours': '14', 'minutes': '10'}, 'name': 'TCS Lab'},
                {'start': {'hours': '16', 'minutes': '30'}, 'end': {'hours': '18', 'minutes': '00'}, 'name': 'Table Tennis Training'}
                ]
    def __init__(self):
        pass

    @staticmethod
    def lessonToString(lesson):
        return f"{lesson['start']['hours']}:{lesson['start']['minutes']}-{lesson['end']['hours']}:{lesson['end']['minutes']}: {lesson['name']}"

    def show_schedule(self):
        res = ''
        current = getCorrectDate()
        for lesson in self.schedule:
            if int(lesson['end']['hours']) * 3600 + int(lesson['end']['minutes']) * 60 > current.hour * 3600 + current.minutes * 60 + current.second:
                res = res + '✅' + Thursday.lessonToString(lesson) + '\n'
            else:
                res = res + '❌' + Thursday.lessonToString(lesson) + '\n'
        return res
    

class Friday:
    schedule = [{'start': {'hours': '09', 'minutes': '00'}, 'end': {'hours': '10', 'minutes': '30'}, 'name': 'AGLA Lecture'},
                {'start': {'hours': '10', 'minutes': '40'}, 'end': {'hours': '12', 'minutes': '10'}, 'name': 'AGLA Tutorial'},
                {'start': {'hours': '12', 'minutes': '40'}, 'end': {'hours': '14', 'minutes': '10'}, 'name': 'AGLA Lab'}
                ]
    def __init__(self):
        pass

    @staticmethod
    def lessonToString(lesson):
        return f"{lesson['start']['hours']}:{lesson['start']['minutes']}-{lesson['end']['hours']}:{lesson['end']['minutes']}: {lesson['name']}"

    def show_schedule(self):
        res = ''
        current = getCorrectDate()
        for lesson in self.schedule:
            if int(lesson['end']['hours']) * 3600 + int(lesson['end']['minutes']) * 60 > current.hour * 3600 + current.minutes * 60 + current.second:
                res = res + '✅' + Friday.lessonToString(lesson) + '\n'
            else:
                res = res + '❌' + Friday.lessonToString(lesson) + '\n'
        return res
    

class Saturday:
    schedule = [{'start': {'hours': '10', 'minutes': '40'}, 'end': {'hours': '14', 'minutes': '10'}, 'name': 'Software Engineering Toolkit'},]
    def __init__(self):
        pass

    @staticmethod
    def lessonToString(lesson):
        return f"{lesson['start']['hours']}:{lesson['start']['minutes']}-{lesson['end']['hours']}:{lesson['end']['minutes']}: {lesson['name']}"

    def show_schedule(self):
        res = ''
        current = getCorrectDate()
        for lesson in self.schedule:
            if int(lesson['end']['hours']) * 3600 + int(lesson['end']['minutes']) * 60 > current.hour * 3600 + current.minutes * 60 + current.second:
                res = res + '✅' + Saturday.lessonToString(lesson) + '\n'
            else:
                res = res + '❌' + Saturday.lessonToString(lesson) + '\n'
        return res
    

class Sunday:
    schedule = [{'start': {'hours': '11', 'minutes': '30'}, 'end': {'hours': '13', 'minutes': '00'}, 'name': 'DSA Lecture'},]
    def __init__(self):
        pass

    @staticmethod
    def lessonToString(lesson):
        return f"{lesson['start']['hours']}:{lesson['start']['minutes']}-{lesson['end']['hours']}:{lesson['end']['minutes']}: {lesson['name']}"

    def show_schedule(self):
        res = ''
        current = getCorrectDate()
        for lesson in self.schedule:
            if int(lesson['end']['hours']) * 3600 + int(lesson['end']['minutes']) * 60 > current.hour * 3600 + current.minutes * 60 + current.second:
                res = res + '✅' + Sunday.lessonToString(lesson) + '\n'
            else:
                res = res + '❌' + Sunday.lessonToString(lesson) + '\n'
        return res
    

schedule = {
    0: Monday(),
    1: Tuesday(),
    2: Wednesday(),
    3: Thursday(),
    4: Friday(),
    5: Saturday(),
    6: Sunday()
}

'''DSA Lecture\n10:40-12:10 DSA Tutorial\n12:40-14:10 DSA Lab\n16:00-17:30: AWA',
    '09:00-10:30 SSAD Lecture\n10:40-12:10 SSAD Tutorial\n14:20-15:50 SSAD Lab\n16:30-18:00: Table Tennis Training',
    '09:00-10:30 Math Analysis Lecture\n10:40-12:10 Math Analysis Tutorial\n12:40-14:10 Math Analysis Lab\n16:00-17:30: AWA',
    '09:00-10:30 TCS Lecture\n10:40-12:10 TCS Tutorial\n12:40-14:10 TCS Lab\n16:30-18:00: Table Tennis Training',
    '09:00-10:30 AGLA Lecture\n10:40-12:10 AGLA Tutorial\n12:40-14:10 AGLA Lab',
    '10:40-14:10 Software Engineering Toolkit',
    '11:30-13:00 Table Tennis Tournament'''

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

def getCorrectDate():
    old = (datetime.now() - datetime(1970, 1, 1, 0, 0, 0, 0)).total_seconds() + 10800
    new = datetime.fromtimestamp(old)
    return new

@t.message_handler(commands=['start'])
def start(message):
    t.send_message(message.chat.id, "Привет! Чтобы я показывал правильное время, пришли мне свою геопозицию (кнопку в меню), а затем используй /date или /schedule.")

@t.message_handler(commands=['schedule'])
def send_schedule(message):
    if not check_subscription(message):
        return
    t.send_message(message.chat.id, schedule[getCorrectDate().weekday()].showSchedule())

@t.message_handler(commands=['date'])
def send_date(message):
    if not check_subscription(message):
        return
    t.send_message(message.chat.id, toString(getCorrectDate()))

t.infinity_polling()