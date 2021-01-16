endNum = int(input('Введите конечное число: '))
for col in range(1, endNum + 1):
    for row in range(1, endNum +1):
        if row % 3 == 0:
            print(row, end=' ')
        else:
            print(col, end=' ')
    print()