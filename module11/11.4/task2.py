import math

distance = float(input('Введите расстояние до вражеского танка: '))
angle = float(input('Введите угол поворота: '))

angle /= 57.2958

a = math.sin(angle) * distance
b = math.cos(angle) * distance

print('Координаты вражеского танка: (' + str(a) + ', ' + str(b) + ')')