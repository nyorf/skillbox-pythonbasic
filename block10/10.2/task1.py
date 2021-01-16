matrixSize = int(input('Введите размер матрицы: '))
for col in range(1, matrixSize + 1):
    for row in range(1, matrixSize + 1):
        if col % 2 == 0:
            print(col, end=' ')
        else:
            print(row, end=' ')
    print()