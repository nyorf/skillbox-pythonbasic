distance = int(input('Введите дистанцию первого дня: '))
goal = int(input('Сколько километров нужно пробежать? '))
daycounter = 0
while distance < goal:
    tenpercent = distance * 0.1
    distance += tenpercent
    daycounter += 1
print('Чтобы пробежать', goal, 'километров у спортсмена уйдёт', daycounter, 'дней')
