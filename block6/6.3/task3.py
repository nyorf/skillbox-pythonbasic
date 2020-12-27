number = int(input('Введите число: '))
counter = 0
while number >= 0:
    counter += 1
    number = int(input('Введите ещё число: '))
print('Всего было введено чисел:', counter)
