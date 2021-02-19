hourDegree = float(input('Введите угол: '))
currentHour = int(hourDegree / 30)
minutesPassedCH = (hourDegree - currentHour * 30) / 0.5
print('Минутная стрелка повернулась на', minutesPassedCH * 6, 'градусов за последний час')

