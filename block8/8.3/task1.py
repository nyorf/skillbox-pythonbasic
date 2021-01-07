stopNum = int(input('Введите конечное число: '))
for number in range(1, stopNum + 1, 2):
    print('Третья степень числа', number, '=', number ** 3)