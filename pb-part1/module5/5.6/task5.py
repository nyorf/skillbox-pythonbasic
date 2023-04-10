dayoftheweek = int(input('Введите номер дня недели: '))
timeremaining = int(input('Введите количество часов до конца рабочего дня: '))
if dayoftheweek == 1:
    print('Сегодня понедельник.')
elif dayoftheweek == 2:
    print('Сегодня вторник.')
elif dayoftheweek == 3:
    print('Сегодня среда.')
elif dayoftheweek == 4:
    print('Сегодня четверг.')
elif dayoftheweek == 5:
    print('Сегодня пятница.')
elif dayoftheweek == 6:
    print('Сегодня суббота.')
else:
    print('Сегодня воскресенье.')
if dayoftheweek == 5:
    if timeremaining < 2:
        print('Осталось работать', timeremaining, 'час(ов). Сегодня можно уйти пораньше!')
    else:
        print('Осталось работать', timeremaining, 'час(ов).')
else:
    print('Осталось работать', timeremaining, 'час(ов).')
