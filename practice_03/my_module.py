import json
from hashlib import sha256
import datetime as dt

db = {}

def save_db():
    """Функция, сохраняющая базу данных в json файл
     с названием "db.json", возле файла модуля.
     """
    # global db
    with open('db.json', 'w') as file_db:
        json.dump(db, file_db, indent=2, ensure_ascii=False)


def load_db():
    """Функция загружающая данные из файла базы
     данных в глобальную переменную с базой данных"""
    global db
    try:
        with open('db.json') as json_file:
            try:
                db = json.load(json_file)
            except:
                db = {}
    except:
        db = {}


def encrypt(string):
    signature = sha256(string.encode()).hexdigest()
    return signature


def write_new_login(login, password, email):
    """Функция внесения данных про нового пользователя.
    Принимает 3 аргумента: (login, password, email).
     вносит данные в словарь в установленном виде.
     Возвращает True, если данные внесены, иначе False.
      Данные не могут быть внесены, если такой login уже существует в бд.
       После успешного внесения данных, вызывает функцию сохранения базы данных в файл.
       Пароль должен сохраняться в базе данных, в зашифрованом виде,
       используем модуль hashlib для реализации этого требования."""

    load_db()
    global db
    password_s = encrypt(password)
    if login not in db:
        login_dict = {
            'password': password_s,
            'email': email,
            'notes': []
        }
        db[login] = login_dict
        save_db()
        return True
    else:
        return False


def is_valid_login(login, password):
    """Функция проверяющая возможность авторизации.
 Принимает 2 аргумента (login, password).
 Если login и password обнаружены в базе данных, возвращает True, иначе False. Помним о том, что пароль в базе данных, находится в зашифрованом виде.
"""
    load_db()
    global db
    password_s = encrypt(password)
    if db:
        if login in db and password_s == db[login]['password']:
            return True
        else:
            return False
    else:
        return False


def get_notes(login):
    """Функция, возвращающая заметки в виде списка из двух значений
 - где первое значение - номер заметки, начиная с единицы,
 где второе - словарь содержащий саму заметку.
Принимает один  аргумент (login).
"""
    # load_db()
    global db
    notes_list = db[login]['notes']
    n_list = []

    if not notes_list:
        return []

    n = 1
    for i in notes_list:
        n_tuple = (n, i)
        n_list.append(n_tuple)
        n += 1
    return n_list


def add_note(login, title='', text=''):
    """Функция добавляющая данные новой заметки в базу данных.
     Принимает 3 аргумента (login, title, body).
      Заметка будет иметь название(title) и текст(body).
       Заметка должна добавляться в виде словаря в список под ключем notes
        по переданному login. Словарь имеет следующую структуру:
    {'title': 'blablabla', 'body': 'text', 'datetime': '01.01.2018 - 23:59:59'}
    При добавлении данных заметки в базу данных, добавляем дату и время создания заметки.
     Для этого используем модуль datetime.
     После добавления данных, используем функцию сохранения базы данных в файл.
    """
    # load_db()
    global db
    notes_lst = db[login]['notes']
    note_dic = {
        'title': title,
        'text': text,
        'datetime': dt.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    }
    notes_lst.append(note_dic)

    db[login]['notes'] = notes_lst
    save_db()


def delete_note(login, num):
    """Функция удаляющая заметку по номеру заметки.
    Где номер - index+1 Т.Е. нумерация заметок начинается с единицы,
    это необходимо учитывать.
    Принимает два аргумента (login, num).
    Удаляет заметку из notes по переданному login.
    После удаления заметки, используем функцию сохранения базы данных в файл."""
    # load_db()
    global db
    notes_list = db[login]['notes']
    try:
        note = notes_list.pop(num - 1)
        db[login]['notes'] = notes_list
        save_db()
        return True
    except:
        return False


def get_note(login, num=0):
    """ Функция, возвращающая словарь
     с данными о заметке по номеру заметки,
     начиная с единицы.
     Принимает два аргумента (login, num).
"""
    # load_db()
    global db
    notes_list = db[login]['notes']

    if num > 0:
        try:
            return notes_list[num - 1]
        except:
            return {}
    else:
        return {}
