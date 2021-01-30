for row in range(20):
    print()
    for col in range(50):
        if col == 24:
            print('|', end='')
        if row + 28 == col and row == 9:
            print('\\', end='')
        elif -row + 19 == col and row == 9:
            print('/', end='')
        elif row == 9:
            print('-', end='')
        elif row + 28 == col:
            print('\\', end='')
        elif -row + 19 == col:
            print('/', end='')
        else:
            print(' ', end='')

