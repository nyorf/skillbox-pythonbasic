def divisionbytwo(number):
    counter = 0
    while number != 0:
        counter += 1
        number /= 2
    return counter

number = int(input('Введите число: '))
print('Число', number, 'можно', divisionbytwo(number), 'раз поделить на 2.')