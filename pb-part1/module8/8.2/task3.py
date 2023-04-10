stopNum = int(input('Введите конечное число: '))
for number in range(1, stopNum // 2 + stopNum % 2 + 1):
    print('Квадрат числа', number * 2 - 1, '=', (number * 2 - 1) ** 2)