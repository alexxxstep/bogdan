'''Пользователь вводит любой текст, состоящий из любых символов, в том числе и русских букв.
Вывести на экран строку транслитом английскими буквами;
Договариваемся о следующей зависимости русско-английских букв:
а - a
б - b
в - v
г - gen
д - d
е - e
ё - e
ж - zh
з - z
к - k
л - l
и - i
й - y
м - m
н - n
о - o
п - p
р - r
с - s
т - t
у - u
ф - f
х - h
ц - c
ч - ch
ш - sh
щ - sch
ь - '
ы - y
ъ - '
э - e
ю - ju
я - ya

Допустим пользователь ввел "Привет", на экран должно вывестись "Privet".
Полезная информация для выполнения.
Используйте словарь для хранения зависимостей букв.
Если вам нужно проверить является ли символ буквой алфавита, для этого можно использовать строчный метод isalpha().

'а'.isalpha()
True
'.'.isalpha()
False
'2'.isalpha()
False
'ь'.isalpha()
True
a = 'б'
a.isalpha()
True

При необходимости проверить букву на верхний регистр, используем метод isupper().
'а'.isupper()
False
'А'.isupper()
True

Аналогично работает метод и для проверки нижнего регистра - islower().
Вернуть строку в верхнем регистре возможно методом upper().
print 'а'.upper()
А

Аналогично работает метод возвращающий строку в нижнем регистре - lower.

Не все методы будут необходимы именно вам, для решения поставленной задачи. Взависимости от логики вашего кода, вам могут понадобиться только некоторые из них.'''

abc_dic = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'gen', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'к': 'k',
           'л': 'l', 'и': 'i', 'й': 'y', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
           'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ь': '\'', 'ы': 'y', 'ъ': '\'', 'э': 'e',
           'ю': 'ju', 'я': 'ya'}

s_txt = input('Input text:')

n_txt = ''
n_list = []
ks = list(abc_dic.keys())
# print(ks)

for i in s_txt:

    if i.isalpha():
        if i.isupper() and i.lower() in ks:
            t = i.lower()
            n = abc_dic[t]
            n_list.append(n.upper())
        elif i.islower() and i in ks:
            n = abc_dic[i]
            n_list.append(n)
        else:
            n_list.append(i)
    else:
        n_list.append(i)

n_txt = ''.join(n_list)

print(n_txt)
