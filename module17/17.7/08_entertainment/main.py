from random import randint

sticks = int(input('Введите количество палок: '))
throws = int(input('Введите количество бросков: '))

row = ['I' for _ in range(sticks)]

for t in range(1, throws + 1):
    R_i = randint(1, sticks)
    L_i = randint(1, R_i)
    row[L_i - 1:R_i] = ['.'] * (R_i - L_i + 1)
    print('Бросок', str(t) + '.', 'Сбиты палки с номера', L_i, 'по', R_i)

print('Результат:', end=' ')
for elem in row:
    print(elem, end='')
