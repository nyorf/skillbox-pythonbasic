def count_letters(text, searchterm_num, searchterm_letter):
    num_count = 0
    letter_count = 0
    for sym in text:
        if sym == str(searchterm_num):
            num_count += 1
        elif sym == str(searchterm_letter):
            letter_count += 1

    print('\nКоличество цифр', str(searchterm_num) + ':', num_count)
    print('Количество букв', searchterm_letter + ':', letter_count)

text = input('Введите текст: ')
searchterm_num = int(input('Какую цифру ищем? '))
searchterm_letter = input('Какую букву ищем? ')

count_letters(text, searchterm_num, searchterm_letter)