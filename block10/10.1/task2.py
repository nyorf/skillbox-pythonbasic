endNum = int(input('Введите число: '))
for col in range(0, endNum + 1):
    for row in range(0, endNum + 1):
        print(row + col, end='\t')
    print()