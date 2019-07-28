import my_module


def choice_registration_login():
    """Функцию, реализующую для пользователя возможность выбор между регистрацией или авторизацией.
    По выбору пользователя, запускается одна из двух выше описанных функций. Работа функции должна быть цикличной.
    """
    choices = ['r', 's', 'e']
    choice = ''
    while choice != 'e':
        print('_' * 50)
        choice = input('Choice command: registration - r, sign in - s, exit - e: ')
        if choice not in choices:
            print('input correct value of command')
            continue

        if choice == 'r':
            registration()
        elif choice == 's':
            sign_in()


def registration():
    """Функция, которая предлогает пользователю зарегистрироваться,
     придумать и ввести login, email и password. Для внесения данных,
      использует соответствующую функцию из первого модуля.
       Выводит пользователю уведомления о успешной или неуспешной регистрации."""
    print('_' * 50)
    data_login = input('Input login - password - email: ')
    data_lst = data_login.split()
    try:
        login = data_lst[0]
        password = data_lst[1]
        email = data_lst[2]

        if my_module.write_new_login(login, password, email):
            print('_' * 50)
            print('You have successfully registered!')
            sign_in()
        else:
            print('_' * 50)
            print('You can not use this login to register. Try again')


    except IndexError:
        print('_' * 50)
        print('uncorrected input. try again')



def sign_in():
    """Функция, занимающаяся авторизацией пользователя.
    Просит ввести login и password.
    Для проверки использует соответствующую функцию из первого модуля."""
    print('_' * 50)
    s_data = input('* input login and password: ')
    s_list = s_data.split()
    try:
        login = s_list[0]
        password = s_list[1]

        if my_module.is_valid_login(login, password):
            print(' ')
            print(f'Hello {login}')
            print(' ')
            note_space(login)
        else:
            print('_' * 50)
            print('*login or password is uncorrected')
    except IndexError:
        print('_' * 50)
        print('uncorrect input')



def note_space(login):
    """Функция работы с пространством заметок.
Принимает один аргумент (login).
Используя выше описанную функцию, выводит на экран список заметок и предлогает пользователю варианты работы с заметками (создать, удалить или прочесть). По выбору пользователя, запускает одну из ниже описанных функций.
Работа функции должна быть цикличной.
"""

    choices = ['c', 'd', 'r', 'e']
    val = ''
    while val != 'e':
        note_list_empty = print_notes(login)
        print('_' * 50)
        if not note_list_empty:
            print('_' * 50)
            val = input('* Choice command: create note - c, delete - d, read - r, exit  - e: ')
        else:
            print('_' * 50)
            val = input('* Choice command: create note - c, exit  - e: ')

        if val not in choices:
            print('input correct value of command')
            continue

        if val == 'c':
            create_note(login)
        elif val == 'd':
            delete_note(login)
        elif val == 'r':
            read_note(login)


def print_notes(login):
    """Функция, выводящая на экран заметки конкретного пользователя в столбик в следующем формате:
номер | название | дата и время
Для получения списка заметок, использует соответствующую функцию из первого модуля. Принимает один аргумент (login).
"""

    note_list = my_module.get_notes(login)
    if note_list:
        print('='*50)
        print('Your notes:')
        for n, i in note_list:
            title = i['title']
            d_time = i['datetime']
            print(f'{n} | {title} | {d_time}')
        return False
    else:
        print('Your notes is empty')
        return True


def create_note(login):
    """Функция создающая заметку. Принимает один аргумент (login).
Предлогает пользователю ввести название и текст заметки.
 Использует соответствующую функцию из первого модуля, для сохранения данных заметки.
"""
    print('_' * 50)
    title = input('title of note: ')
    text = input('text of note: ')
    my_module.add_note(login, title, text)


def delete_note(login):
    """Функция, удаляющая заметку.
    Принимает один аргумент (login(.
     Запрашивает у пользователя номер удаляемой заметки, для удаления,
     использует соответствующую функцию из первого модуля."""
    print('_' * 50)
    num_s = input('number of notes: ')
    if num_s.isdigit():
        if not my_module.delete_note(login, int(num_s)):
            print('uncorrected value number')
    else:
        print('uncorrected value number')


def read_note(login):
    """Функция, удаляющая заметку.
    Принимает один аргумент (login(.
     Запрашивает у пользователя номер удаляемой заметки, для удаления,
     использует соответствующую функцию из первого модуля."""
    print(' ')
    num_s = input('number of notes: ')
    print('_' * 50)
    if num_s.isdigit():
        note_dic = my_module.get_note(login, int(num_s))
        if note_dic:
            title = note_dic['title']
            text = note_dic['text']
            d_time = note_dic['datetime']
            print(f'{title}, {text}, {d_time}')
            print(' ')
        else:
            print('_' * 50)
            print('uncorrected value number')
    else:
        print('_' * 50)
        print('uncorrected value number')


if __name__ == '__main__':
    choice_registration_login()+
