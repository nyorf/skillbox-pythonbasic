matrixSize = int(input('Введите размер матрицы: '))
for row in range(1, matrixSize + 1):
    for col in range(1, matrixSize + 1):
        if row % 2 == 0:
            print(row, end=' ')
        else:
            print(col, end=' ')
    print()