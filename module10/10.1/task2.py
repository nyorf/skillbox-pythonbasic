endNum = int(input('Введите число: '))
for row in range(0, endNum + 1):
    for col in range(0, endNum + 1):
        print(row + col, end='\t')
    print()