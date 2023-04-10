x = float(input('Введите координаты по горизонтали: '))
y = float(input('Введите координаты по вертикали: '))
if (x > 0.8) or (x < 0) or (y > 0.8) or (y < 0):
    print('Вы вышли за пределы доски!')
else:
    xLocation = int(x * 10)
    yLocation = int(y * 10)
    print('Фигура находится в клетке (' + str(xLocation) + ',' + str(yLocation) + ')')