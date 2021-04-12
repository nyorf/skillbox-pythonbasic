message = input('Введите текст: ')
counter = 0
for sym in message:
    counter += 1
    if sym == '*':
        print('Символ "*" стоит на', counter, 'позиции.')
        break
