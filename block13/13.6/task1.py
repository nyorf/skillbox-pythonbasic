def expform(number):
    counter = 0
    if number > 1:
        while not 1 < number < 10:
            counter += 1
            number /= 10
        return number, counter
    elif 0 < number < 1:
        while not 1 < number < 10:
            counter += 1
            number *= 10
        number = round(number, 15)
        counter = '-' + str(counter)
        return number, counter
    elif number < 0:
        print('Число не может быть отрицательным!')
    else:
        return 0

number = float(input('Введите число: '))
expnum, counter = expform(number)
print('Формат плавающей точки: x =', expnum, '* 10 **', counter)