posX = 8
posZ = 10
while True:
    print('[Программа]: Марсоход находится на позиции,', str(posX) + ',', str(posZ), 'введите команду:')
    operator = input('[Оператор]: ')
    if (operator == 'W' or operator == 'w') and posX < 15:
        posX += 1
    elif (operator == 'A' or operator == 'b') and posZ > 0:
        posZ -= 1
    elif (operator == 'S' or operator == 's') and posX > 0:
        posX -= 1
    elif (operator == 'D' or operator == 'd') and posZ < 20:
        posZ += 1
    else:
        print('Марсоход не может двигаться по заданной вами позиции.')
