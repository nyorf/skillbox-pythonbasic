width = int(input('Введите ширину рамки: '))
length = int(input('Введите длину рамки: '))
for row in range(1, length + 1):
    print()
    for col in range(1, width + 1):
        if col == 1 or col == width:
            print('|', end='')
        elif row == 1 or row == length:
            print('-', end='')
        else:
            print(' ', end='')