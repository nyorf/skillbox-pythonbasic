x = float(input('Введите координаты по горизонтали: '))
y = float(input('Введите координаты по вертикали: '))
if (x > 0.8) or (x < 0) or (y > 0.8) or (y < 0):
    print('Вы вышли за пределы доски!')
else:
    xLocation = int(x * 10)
    yLocation = int(y * 10)
    xCentered = (round(x, 1) + 0.05) - x
    yCentered = (round(y, 1) + 0.05) - y
    print('Фигура находится в клетке (' + str(xLocation) + ', ' + str(yLocation) + ')')
    print('Поправьте положение фигуры на (' + str(round(xCentered, 3)) + ', ' + str(round(yCentered, 3)) + ')')