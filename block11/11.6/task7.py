while True:
    print('Введите координаты коня:')
    xKnight = int(float(input('x: ')) * 10)
    yKnight = int(float(input('y: ')) * 10)
    print('\nВведите координаты точки на доске:')
    xPoint = int(float(input('x: ')) * 10)
    yPoint = int(float(input('y: ')) * 10)
    if xPoint < 0 or yPoint < 0 or xKnight < 0 or yPoint < 0: # контроль входа
        print('Вводимые координаты не могут быть отрицательными! Попробуйте снова.\n')
    elif xPoint >= 10 or yPoint >= 10 or xKnight >= 10 or yPoint >= 10:
        print('Вводимые координаты не могут быть >= 1!\n')
    else:
        break
print('\nКонь в клетке (' + str(xKnight) + ',' + str(yKnight) + ').', end=' ')
print('Точка в клетке (' + str(xPoint) + ',' + str(yPoint) + ')')
coordinatesCheck = (xPoint - xKnight) + (yPoint - yKnight)
if coordinatesCheck == 3 or coordinatesCheck == -3:
    # у доступных коню клеток сумма разностей каждой координаты равна либо 3, либо -3
    print('\nДа, конь может ходить в эту точку.')
elif xKnight == xPoint and yKnight == yPoint: # ну а вдруг
    print('\nКонь и так находится в этой точке!')
else:
    print('\nНет, конь не может ходить в эту точку.')