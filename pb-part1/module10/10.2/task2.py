endNum = int(input('Введите конечное число: '))
for row in range(1, endNum + 1):
    for col in range(1, endNum +1):
        if col % 3 == 0:
            print(col, end=' ')
        else:
            print(row, end=' ')
    print()