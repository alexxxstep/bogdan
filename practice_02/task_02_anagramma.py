'''Напишем приложение для игры в анаграмму:
 Правила этой игры довольно старые и простые.
  Человеку предоставляется слово из набора букв,
   которые он должен расставить таким образом,
   чтобы получилось правильное слово.
   Кпримеру: ооаркв - корова тмале - метла
    Способом перестановки букв, находят и составляют корректное слово.

Программа заранее должна содержать набор слов для анаграммы,
 достаточно будет 3-4 слов для проверки.
 Пользователю выводят слово из хаотичного набора букв.
  Все, что может делать пользователь, это указывать какую букву,
  куда переместить.
  Кпримеру: тмале Вторую букву, поставим первой мтале теперь пятую букву,
  поставим второй метал теперь четвертую букву, поставим пятой метла

Программа предоставляет пользовательский ввод,
куда пользователь указывает через пробел номер буквы,
которую нужно переместить и номер буквы, на который нужно переместить
букву: 3 1 - третью букву поставить первой,
1 4 - первую букву поставить четвертой и Т.Д.
Когда пользователь выстроит все буквы правильно,
программа сообщает ему о том, что он молодец и составил слово правильно,
 затем предлогает ему следующее слово и так до тех пор,
 пока заготовленные слова не закончатся.'''
import random

# words = 'уборка стирка материк вход'
words = 'вход рыба'

print(words.upper())

print('='*50)

w_dic = {}

for w in words.split():
    w_letters = list(w)
    random.shuffle(w_letters)

    w_dic[w] = ''.join(w_letters)

for key_w, item_w in w_dic.items():

    print(f'{key_w.upper()} - {item_w.upper()}')
    w_len = len(key_w)
    k = [str(n+1) for n in range(w_len)]
    w_len_str = ''.join(k)
    print(f'{w_len_str} - {w_len_str}')

    while not key_w == item_w:
        numbs = input('move letters with numbers |from| [space] |to| :')
        n_list = numbs.split()
        try:
            n_from = int(n_list[0])
            n_to = int(n_list[1])
        except:
            print('uncorrected input,try again...')
            continue

        w_len = len(key_w)

        if n_from > w_len or n_to > w_len:
            print('uncorrected input,try again...')
            continue

        letters_list = list(item_w)

        l_from = letters_list[n_from - 1]
        l_to = letters_list[n_to - 1]

        letters_list[n_to - 1] = l_from
        letters_list[n_from - 1] = l_to

        item_w = ''.join(letters_list)

        print(item_w.upper())
        print(f'{w_len_str}')

    print('='*50)
    print('Good!!!')
    print(f'{key_w.upper()} - {item_w.upper()}')
    print('=' * 50)

print('-=GAME OVER=-')
