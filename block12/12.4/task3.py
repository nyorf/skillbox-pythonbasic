import math

def selftopoint(x, y):
    distance = math.sqrt(x ** 2 + y ** 2)
    print('Расстояние от вашего местоположения до точки [' + str(x) + ', ' + str(y) + ']:', distance)

def pointtopoint(x1, y1, x2, y2):
    sidea = x2 - x1
    sideb = y2 - y1
    distance = math.sqrt(sidea ** 2 + sideb ** 2)
    print('Расстояние от точки [' + str(x1) + ', ' + str(y1) + '] до точки [' + str(x1) + ', ' + str(y1) + ']:', distance)

decision = int(input('\nНайти расстояние от себя до точки (1) или найти расстояние от точки до точки (2)? '))

if decision == 1:
    x = float(input('Введите координату точки x: '))
    y = float(input('Введите координату точки y: '))
    selftopoint(x, y)
elif decision == 2:
    x1 = float(input('Введите координату точки x1: '))
    y1 = float(input('Введите координату точки y1: '))
    x2 = float(input('Введите координату точки x2: '))
    y2 = float(input('Введите координату точки y2: '))
    pointtopoint(x1, y1, x2, y2)
else:
    print('Введите 1, если хотите найти расстояние от себя до точки, или 2, если хотите найти расстояние от точки до точки.')