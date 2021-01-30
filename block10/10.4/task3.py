endNum = int(input('Введите число: '))
for row in range(endNum + 1):
    print()
    for col in range(endNum + 1):
        printNum = row + col
        if printNum <= endNum:
            print(printNum, end=' ')
        else:
            print(' ', end=' ')