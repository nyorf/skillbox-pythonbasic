import math

def cubicequation(d_subtrahend):
    a = 1
    b = -3
    c = -12
    d = 10 - d_subtrahend
    q = (b ** 2 - 3 * c) / 9
    r = (2 * b ** 3 - 9 * b * c + 27 * d) / 54
    phi = (1 / 3) * math.acos(r / math.sqrt(q ** 3))
    firstroot = -2 * math.sqrt(q) * math.cos(phi) - (b / 3)
    secondroot = -2 * math.sqrt(q) * math.cos(phi + (2 / 3) * math.pi) - (b / 3)
    thirdroot = -2 * math.sqrt(q) * math.cos(phi - (2 / 3) * math.pi) - (b / 3)
    if 0 < firstroot < 4:
        return firstroot
    elif 0 < secondroot < 4:
        return secondroot
    elif 0 < thirdroot < 4:
        return thirdroot
    else:
        return


while True: # контроль ввода
    maxdangerlvl = float(input('Введите максимально допустимый уровень опасности: '))
    if maxdangerlvl < 0:
        print('\nУровень опасности не может быть меньше нуля!')
    else:
        break

result = cubicequation(maxdangerlvl)
if result == 0:
    print('С таким уровнем опасности сделать кладку не получится.')
else:
    print('Приблизительная глубина безопасной кладки:', result)