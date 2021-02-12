import math
earthV = 10.8321 * 10 ** 11
r = float(input('Введите радиус планеты: '))
v = (4 * math.pi / 3) * r ** 3
if earthV < v:
    print('Объём планеты Земля меньше в ', round(v / earthV, 3), 'раз')
elif earthV > v:
    print('Объём планеты Земля больше в', round(earthV / v, 3), 'раз')
else:
    print('Объёмы планет равны!')