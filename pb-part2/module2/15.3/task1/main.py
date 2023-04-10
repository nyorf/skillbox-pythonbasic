stringtolist = list(input('Введите строку: '))

current_index = -1
changes_counter = 0
for sym in stringtolist:
    current_index += 1
    if sym == ':':
        stringtolist[current_index] = ';'
        changes_counter += 1

print('\nИсправленная строка:', end=' ')
for sym in stringtolist:
    print(sym, end='')

print('Количество замен:', changes_counter)