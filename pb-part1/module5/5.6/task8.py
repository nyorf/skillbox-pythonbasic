guess_num1 = int(input('Загадайте первое число: '))
guess_num2 = int(input('Загадайте второе число: '))
if (guess_num1 % 2 == 0) or (guess_num2 % 2 == 0):
    print('Одно из чисел - чётное! Учитель заслужил конфету!')
else:
    print('Оба числа - нечётные! Учитель отдаёт конфету!')