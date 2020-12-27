num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))
if num1 > num2 and num1 > num3:
    print('Наибольшее число -', num1)
elif num2 > num3:
    print('Наибольшее число -', num2)
else:
    print('Наибольшее число -', num3)