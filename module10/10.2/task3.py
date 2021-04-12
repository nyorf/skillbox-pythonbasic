for y in range(20):
    for x in range(50):
        if y == 9 and x == 24:
            print('+', end='')
        elif y == 9:
            print('-', end='')
        elif x == 24:
            print('|', end='')
        else:
            print(' ', end='')
    print()