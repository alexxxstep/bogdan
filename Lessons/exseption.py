while True:
    s = input('Введите два     числа через пробел: ').split()

    try:
        a = int(s[0])
    except IndexError:
        print('index error')
    except TypeError:
        print('type error')

    try:
        b = int(s[1])
    except IndexError:
        print('index error')
    except TypeError:
        print('type error')
    except SyntaxError:
        print('syntax  error')
    try:
        c = a / b

    except TypeError:
        print('type error')
    except ZeroDivisionError:
        print('0 division error')

    try:
        print(c)
    except NameError:
        print('name error')
