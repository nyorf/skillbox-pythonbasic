rows = int(input('Введите количество рядов: '))
seats = int(input('Введите количество сидений в ряду: '))
space = int(input('Введите количество метров между рядами: '))
print('Сцена\n')
for row in range(rows):
    print('=' * seats, end=' ')
    print('*' * space, end=' ')
    print('=' * seats)