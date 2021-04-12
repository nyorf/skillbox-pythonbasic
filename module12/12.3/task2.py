import math

def sphereArea(radius):
    s = 4 * math.pi * radius ** 2
    print('\nПлощадь планеты =', s)
def sphereVolume(radius):
    v = (4 / 3) * math.pi * radius ** 2
    print('\nОбъём планеты =', v)

radius = float(input('Введите радиус: '))
sphereArea(radius)
sphereVolume(radius)