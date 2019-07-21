'''Предложить пользовательский ввод, где пользователь может вводить слова, разделенные пробелом, в следующем формате:
Слово должно вводиться в парных символах @@ или ||.
Т.Е.
@bla@
|bla|
правильно
@bla|
|bla@
|bla
@bla
bla@
bla|
bla
неправильно

Необходимо исправить все неправильные варианты следующим образом.
Если знаки непарные Т.Е. @| или |@. Необходимо знак в конце слова, заменить на такой же, как вначале слова.
Если знака вначале или в конце нехватает, необходимо подставить с нужной стороны парный существующему знак.
Если знаков нет совсем, подставляем символы |.
В каждой паре знаков, может быть только одно слово. Строка может представлять из себя:
|bla| @lkj@ @te| |wer@ qwerty| |luty tyty|
И Т.Д.
Написать код, который выправит все неверные места и выведет результат на экран.'''

txt_in = input('input text of words with symbols @ or |: @word1@ |word2| :')

print(txt_in)

symb_keys = ['@', '|']

txt_list = txt_in.split()
txt_out_list = []

for word in txt_list:
    print(word)

    first_s = word[0]
    last_s = word[-1]

    if first_s in symb_keys and last_s in symb_keys:
        if first_s == last_s:
            txt_out_list.append(word)
        else:
            new_word = word.replace(last_s, first_s)
            txt_out_list.append(new_word)
    elif first_s in symb_keys and last_s not in symb_keys:
        new_word = word + first_s
        txt_out_list.append(new_word)
    elif first_s not in symb_keys and last_s in symb_keys:
        new_word = last_s + word
        txt_out_list.append(new_word)
    elif first_s not in symb_keys and last_s not in symb_keys:
        new_word = '|' + word + '|'
        txt_out_list.append(new_word)

text_out = ' '.join(txt_out_list)

print(text_out)
