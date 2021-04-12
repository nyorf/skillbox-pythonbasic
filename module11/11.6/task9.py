import math

print('Даны коэффициенты:')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
discriminant = (b ** 2) - (4 * a * c) # формула дискриминанта
if discriminant == 1: # один корень
    root = (-b + math.sqrt(discriminant)) / (2 * a)
    print('\nКорень уравнения =', root)
elif discriminant == 0: # при нуле корней нет
    print('\nКорней нет!')
else: # всё остальное - 2 корня
    firstroot = (-b + math.sqrt(discriminant)) / (2 * a)
    secondroot = (-b - math.sqrt(discriminant)) / (2 * a)
    if firstroot > secondroot:
        print('\nКорни уравнения:')
        print('x1 =', firstroot, '\nx2 =', secondroot)
    else:
        print('\nКорни уравнения:')
        print('x1 =', secondroot, '\nx2 =', firstroot)