currentDay = input('Введите день недели: ')
dayNum = 0
if (currentDay == 'Понедельник') or (currentDay == 'понедельник'):
    dayNum = 1
elif (currentDay == 'Вторник') or (currentDay == 'вторник'):
    dayNum = 2
elif (currentDay == 'Среда') or (currentDay == 'среда'):
    dayNum = 3
elif (currentDay == 'Четверг') or (currentDay == 'четверг'):
    dayNum = 4
elif (currentDay == 'Пятница') or (currentDay == 'пятница'):
    dayNum = 5
elif (currentDay == 'Суббота') or (currentDay == 'суббота'):
    dayNum = 6
elif (currentDay == 'Воскресенье') or (currentDay == 'воскресенье'):
    dayNum = 7
print('Номер дня недели:', dayNum)