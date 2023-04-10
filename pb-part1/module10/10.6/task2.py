number = int(input('Введите число: '))
for row in range(1, number + 1):
    print()
    for col in range(1, row + 1):
        print(str(row), end=' ')