side = int(input('Введите сторону квадрата: '))
for row in range(side):
    print()
    for col in range(side):
        if -row + side-1 == col:
            print('^', end='')
        elif row == col:
            print('^', end='')
        else:
            print(' ', end='')