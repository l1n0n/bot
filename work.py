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
                {'start': {'hours': '12', 'minutes': '40'}, 'end': {'hours': '14', 'minutes': '10'}, 'name': 'DSA Lab'}
                ]
    def __init__(self):
        pass

    @staticmethod
    def lessonToString(lesson):
        return f"{lesson['start']['hours']}:{lesson['start']['minutes']}-{lesson['end']['hours']}:{lesson['end']['minutes']}: {lesson['name']}"

    def show_schedule(self, current):
        res = ''
        dayIsOver = True
        for lesson in self.schedule:
            if int(lesson['end']['hours']) * 3600 + int(lesson['end']['minutes']) * 60 <= current.hour * 3600 + current.minute * 60 + current.second:
                res = res + '✅' + Monday.lessonToString(lesson) + '\n'
            elif int(lesson['start']['hours']) * 3600 + int(lesson['start']['minutes']) * 60 <= current.hour * 3600 + current.minute * 60 + current.second < int(lesson['end']['hours']) * 3600 + int(lesson['end']['minutes']) * 60:
                res = res + '🧑‍💻' + Monday.lessonToString(lesson) + '\n'
                dayIsOver = False
            else:
                res = res + '❌' + Monday.lessonToString(lesson) + '\n'
                dayIsOver = False
        return res + '\nНа сегодня занятия закончились! 🥳' if dayIsOver else res
    

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

    def show_schedule(self, current):
        res = ''
        dayIsOver = True
        for lesson in self.schedule:
            if int(lesson['end']['hours']) * 3600 + int(lesson['end']['minutes']) * 60 <= current.hour * 3600 + current.minute * 60 + current.second:
                res = res + '✅' + Tuesday.lessonToString(lesson) + '\n'
            elif int(lesson['start']['hours']) * 3600 + int(lesson['start']['minutes']) * 60 <= current.hour * 3600 + current.minute * 60 + current.second < int(lesson['end']['hours']) * 3600 + int(lesson['end']['minutes']) * 60:
                if 'Tennis' not in lesson['name']:
                    res = res + '🧑‍💻' + Tuesday.lessonToString(lesson) + '\n'
                else:
                    res = res + '🏓' + Tuesday.lessonToString(lesson) + '\n'
                dayIsOver = False
            else:
                res = res + '❌' + Tuesday.lessonToString(lesson) + '\n'
                dayIsOver = False
        return res + '\nНа сегодня занятия закончились! 🥳' if dayIsOver else res


class Wednesday:
    schedule = [{'start': {'hours': '09', 'minutes': '00'}, 'end': {'hours': '10', 'minutes': '30'}, 'name': 'Math Analysis Lecture'},
                {'start': {'hours': '10', 'minutes': '40'}, 'end': {'hours': '12', 'minutes': '10'}, 'name': 'Math Analysis Tutorial'},
                {'start': {'hours': '12', 'minutes': '40'}, 'end': {'hours': '14', 'minutes': '10'}, 'name': 'Math Analysis Lab'}
                ]
    def __init__(self):
        pass

    @staticmethod
    def lessonToString(lesson: dict) -> str:
        return f"{lesson['start']['hours']}:{lesson['start']['minutes']}-{lesson['end']['hours']}:{lesson['end']['minutes']}: {lesson['name']}"

    def show_schedule(self, current) -> str:
        res = ''
        dayIsOver = True
        for lesson in self.schedule:
            if int(lesson['end']['hours']) * 3600 + int(lesson['end']['minutes']) * 60 <= current.hour * 3600 + current.minute * 60 + current.second:
                res = res + '✅' + Wednesday.lessonToString(lesson) + '\n'
            elif int(lesson['start']['hours']) * 3600 + int(lesson['start']['minutes']) * 60 <= current.hour * 3600 + current.minute * 60 + current.second < int(lesson['end']['hours']) * 3600 + int(lesson['end']['minutes']) * 60:
                res = res + '🧑‍💻' + Wednesday.lessonToString(lesson) + '\n'
                dayIsOver = False
            else:
                res = res + '❌' + Wednesday.lessonToString(lesson) + '\n'
                dayIsOver = False
        return res + '\nНа сегодня занятия закончились! 🥳' if dayIsOver else res
    

class Thursday:
    schedule = [{'start': {'hours': '09', 'minutes': '00'}, 'end': {'hours': '10', 'minutes': '30'}, 'name': 'TCS Lecture'},
                {'start': {'hours': '10', 'minutes': '40'}, 'end': {'hours': '12', 'minutes': '10'}, 'name': 'TCS Tutorial'},
                {'start': {'hours': '12', 'minutes': '40'}, 'end': {'hours': '14', 'minutes': '10'}, 'name': 'TCS Lab'},
                {'start': {'hours': '16', 'minutes': '30'}, 'end': {'hours': '18', 'minutes': '00'}, 'name': 'Table Tennis Training'}
                ]
    def __init__(self):
        pass

    @staticmethod
    def lessonToString(lesson) -> str:
        return f"{lesson['start']['hours']}:{lesson['start']['minutes']}-{lesson['end']['hours']}:{lesson['end']['minutes']}: {lesson['name']}"

    def show_schedule(self, current):
        res = ''
        dayIsOver = True
        for lesson in self.schedule:
            if int(lesson['end']['hours']) * 3600 + int(lesson['end']['minutes']) * 60 <= current.hour * 3600 + current.minute * 60 + current.second:
                res = res + '✅' + Thursday.lessonToString(lesson) + '\n'
            elif int(lesson['start']['hours']) * 3600 + int(lesson['start']['minutes']) * 60 <= current.hour * 3600 + current.minute * 60 + current.second < int(lesson['end']['hours']) * 3600 + int(lesson['end']['minutes']) * 60:
                if 'Tennis' not in lesson['name']:
                    res = res + '🧑‍💻' + Thursday.lessonToString(lesson) + '\n'
                else:
                    res = res + '🏓' + Thursday.lessonToString(lesson) + '\n'
                dayIsOver = False
            else:
                res = res + '❌' + Thursday.lessonToString(lesson) + '\n'
                dayIsOver = False
        return res + '\nНа сегодня занятия закончились! 🥳' if dayIsOver else res
    

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

    def show_schedule(self, current):
        res = ''
        dayIsOver = True
        for lesson in self.schedule:
            if int(lesson['end']['hours']) * 3600 + int(lesson['end']['minutes']) * 60 <= current.hour * 3600 + current.minute * 60 + current.second:
                res = res + '✅' + Friday.lessonToString(lesson) + '\n'
            elif int(lesson['start']['hours']) * 3600 + int(lesson['start']['minutes']) * 60 <= current.hour * 3600 + current.minute * 60 + current.second < int(lesson['end']['hours']) * 3600 + int(lesson['end']['minutes']) * 60:
                res = res + '🧑‍💻' + Friday.lessonToString(lesson) + '\n'
                dayIsOver = False
            else:
                res = res + '❌' + Friday.lessonToString(lesson) + '\n'
                dayIsOver = False
        return res + '\nНа сегодня занятия закончились! 🥳' if dayIsOver else res
    

class Saturday:
    def __init__(self):
        pass

    def show_schedule(self, d: datetime):
        return 'Сегодня ничего нет'
    

class Sunday:
    schedule = [{'start': {'hours': '11', 'minutes': '30'}, 'end': {'hours': '13', 'minutes': '00'}, 'name': 'Table Tennis Tournament'},]
    def __init__(self):
        pass

    @staticmethod
    def lessonToString(lesson):
        return f"{lesson['start']['hours']}:{lesson['start']['minutes']}-{lesson['end']['hours']}:{lesson['end']['minutes']}: {lesson['name']}"

    def show_schedule(self, current):
        res = ''
        dayIsOver = True
        for lesson in self.schedule:
            if int(lesson['end']['hours']) * 3600 + int(lesson['end']['minutes']) * 60 <= current.hour * 3600 + current.minute * 60 + current.second:
                res = res + '✅' + Sunday.lessonToString(lesson) + '\n'
            elif int(lesson['start']['hours']) * 3600 + int(lesson['start']['minutes']) * 60 <= current.hour * 3600 + current.minute * 60 + current.second < int(lesson['end']['hours']) * 3600 + int(lesson['end']['minutes']) * 60:
                res = res + '🏓' + Sunday.lessonToString(lesson) + '\n'
                dayIsOver = False
            else:
                res = res + '❌' + Sunday.lessonToString(lesson) + '\n'
                dayIsOver = False
        return res + '\nНа сегодня занятия закончились! 🥳' if dayIsOver else res


class FieldException(Exception):
    pass

days = {
    0: Monday(),
    1: Tuesday(),
    2: Wednesday(),
    3: Thursday(),
    4: Friday(),
    5: Saturday(),
    6: Sunday()
}

weekdays = 'Понедельник Вторник Среда Четверг Пятница Суббота Воскресенье'.split()

def toString(d: datetime):
    return f'''Сейчас в Иннополисе:\n{weekdays[d.weekday()]}, {d.day:02d}.{d.month:02d}.{d.year}, {d.hour:02d}:{d.minute:02d}:{d.second:02d}''' 

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
    t.send_message(message.chat.id, "Привет! Я бот, который может показывать сегодняшнее расписание лекций в Университете Иннополис.\n\nЧтобы узнать сегодняшнюю дату, нажмите сюда: /date\n\nЧтобы узнать сегодняшнее расписание, нажмите сюда: /schedule")

@t.message_handler(commands=['schedule'])
def send_schedule(message):
    if not check_subscription(message):
        return
    correct = getCorrectDate()
    t.send_message(message.chat.id, days[correct.weekday()].show_schedule(correct))

@t.message_handler(commands=['date'])
def send_date(message):
    if not check_subscription(message):
        return
    t.send_message(message.chat.id, toString(getCorrectDate()))

# @t.message_handler(commands=['game'])
# def game(message):
#     if not check_subscription(message):
#         return
#     field = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]

#     t.send_message(message.chat.id, """Добро пожаловать на игру Крестики-нолики! Не хотите сыграть со мной? Правда, я пока плох в этом, но обещаю скоро научиться.\n
#     Чтобы поставить крестик или нолик напишите в чат координаты, например, 2 1, где 2 - это номер ряда, 1 - это номер столбца.""")

#     gameOver = False

#     def check_field(s):
#         nonlocal gameOver
#         if field[0][0] == field[0][1] == field[0][2] == s or field[1][0] == field[1][1] == field[1][2] == s or field[2][0] == field[2][1] == field[2][2] == s or \
#         field[0][0] == field[1][0] == field[2][0] == s or field[0][1] == field[1][1] == field[2][1] == s or field[0][2] == field[1][2] == field[2][2] == s or \
#         field[0][0] == field[1][1] == field[2][2] == s or field[0][2] == field[1][1] == field[2][0] == s:
#             return True
#         return False
    
#     def show_field():
#         t.send_message(message.chat.id, f"{''.join(field[0])}\n{''.join(field[1])}\n{''.join(field[2])}")
    

    # def process():
    #     x, y = map(int, message.text.split())
    #     try:
    #         if 1 <= x <= 3 and 1 <= y <= 3 and field[x-1][y-1] != '.':
    #             field[x-1][y-1] = 'X'
    #             show_field()
    #             if check_field('X'):
    #                 t.send_message(message.chat.id, 'Game over')
    #                 return
    #             while True:
    #                 xb = randint(0, 2)
    #                 yb = randint(0, 2)
    #                 if field[xb][yb] != '.':
    #                     field[xb][yb] = 'O'
    #                     break
    #             show_field()
    #             if check_field('O'):
    #                 t.send_message(message.chat.id, 'Game over')
    #                 return
    #         else:
    #             raise FieldException
    #     except FieldException:
    #         t.send_message(message.chat.id, 'Введите другую ячейку')
    #         process()
    # process()

games = {}

def check_field(field, s):
    if field[0][0] == field[0][1] == field[0][2] == s or field[1][0] == field[1][1] == field[1][2] == s or field[2][0] == field[2][1] == field[2][2] == s or \
    field[0][0] == field[1][0] == field[2][0] == s or field[0][1] == field[1][1] == field[2][1] == s or field[0][2] == field[1][2] == field[2][2] == s or \
    field[0][0] == field[1][1] == field[2][2] == s or field[0][2] == field[1][1] == field[2][0] == s:
        return True
    return False

def show_field_text(field):
    return f"{''.join(field[0])}\n{''.join(field[1])}\n{''.join(field[2])}"

@t.message_handler(commands=['game'])
def start_game(message):
    user_id = message.from_user.id
    games[user_id] = {
        'field': [['.' for _ in range(3)] for _ in range(3)],
        'counter': 0
    }
    t.send_message(user_id, "Welcome to Tic Tac Toe game. Choose field to place X by entering coordinates in form 2 1, where 2 is row and 1 is column X will be placed")
    t.send_message(user_id, show_field_text(games[user_id]['field']))

@t.message_handler(func=lambda message: message.from_user.id in games)
def handle_move(message):
    user_id = message.from_user.id
    game = games[user_id]
    
    try:
        x, y = map(int, message.text.split())
        if not (1 <= x <= 3 and 1 <= y <= 3 and game['field'][x-1][y-1] == '.'):
            t.send_message(user_id, "Enter another coordinates")
            return
    except:
        t.send_message(user_id, "Enter coordinates in form 2 1")
        return

    game['field'][x-1][y-1] = 'X'
    game['counter'] += 1

    if check_field(game['field'], 'X'):
        t.send_message(user_id, f"{show_field_text(game['field'])}\n\nX win")
        del games[user_id]
        return

    if game['counter'] < 9:
        xb, yb = randint(0, 2), randint(0, 2)
        while game['field'][xb][yb] != '.':
            xb, yb = randint(0, 2), randint(0, 2)
        game['field'][xb][yb] = 'O'
        game['counter'] += 1

        if check_field(game['field'], 'O'):
            t.send_message(user_id, f"{show_field_text(game['field'])}\n\nO win")
            del games[user_id]
            return

    if game['counter'] == 9 and user_id in games:
        t.send_message(user_id, f"{show_field_text(game['field'])}\n\nTie")
        del games[user_id]
    elif user_id in games:
        t.send_message(user_id, show_field_text(game['field']))

t.infinity_polling()