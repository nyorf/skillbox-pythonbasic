size = int(input('Введите размер квадратной матрицы: '))
for row in range(size):
    print()
    for col in range(size):
        if -row + size - 1 == col:
            print('1', end=' ')
        elif -row + size -1 < col:
            print('2', end=' ')
        else:
            print('0', end=' ')