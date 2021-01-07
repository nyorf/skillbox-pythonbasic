chairSumm = 0
lastChair = int(input('Введите последний номер стула: '))
for chair in range(1, lastChair + 1, 5):
    print('Номер стула:', chair)
    chairSumm += chair
print('Сумма:', chairSumm)