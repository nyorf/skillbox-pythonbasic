x_coord = int(input('Введите координату X: '))
y_coord = int(input('Введите координату Y: '))
if x_coord > y_coord:
    print('X больше Y')
if x_coord < y_coord:
    print('Y больше X')
if x_coord == y_coord:
    print('X равен Y')