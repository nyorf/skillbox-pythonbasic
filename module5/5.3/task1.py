x_coord = int(input('Введите координату X: '))
y_coord = int(input('Введите координату Y: '))
if x_coord > y_coord:
    print('X больше Y')
elif x_coord < y_coord:
    print('X меньше Y')
else:
    print('X равен Y')