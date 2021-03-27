"""
not working
"""

def formulae(x):
    return x ** 3 - 3 * x ** 2 - 12 * x + 10


while True:
    dangermaxlvl = float(input('Введите максимально допустимый уровень опасности: '))
    if dangermaxlvl < 0:
        print('\nУровень опасности не может быть меньше нуля!')
    else:
        break

x = 1e-10

while abs(formulae(x, dangermaxlvl)) != dangermaxlvl:
    x += 1e-10
