import math
a = float(input('Введите сторону a: '))
b = float(input('Введите сторону b: '))
c = float(input('Введите сторону c: '))

p = (a + b + c) / 2

s = math.sqrt(p * (p - a) * (p - b) * (p - c))

print('Площадь треугольника:', round(s, 2))