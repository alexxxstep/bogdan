''' Предложить пользовательский ввод, где пользователь может вводить
 ряд чисел через пробел, причем должно соблюдаться жесткое правило,
 каждая последующая цифра должна быть в два раза больше или в два раза меньше чем предыдущая.
  Если встретилась цифра, которая не соответствует этому условию, необходимо вывести порядковый номер цифры,
   которая нарушила условие, а также вывести саму цифру и предыдущую цифру на экран.
    В случае необходимости создания списка натуральных чисел в определенном диапазоне,
     используется функция range().'''

numbs = input('input list of numbers with spase when: n n**2 or n//2...')

n_lst = [int(i) for i in numbs.split() if i.isdigit()]

print(n_lst)

elements = len(n_lst)
print(elements)

for i in range(1, elements):
    prev_n = n_lst[i - 1]
    curr_n = n_lst[i]

    if curr_n == prev_n * 2 or curr_n == prev_n / 2:
        continue

    print(f'in position {i + 1} number {curr_n} in not condition to previos {prev_n}')
