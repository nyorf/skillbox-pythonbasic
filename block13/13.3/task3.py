def floatnum(number):
    counter = 0
    for _ in str(number):
        counter += 1
    number = number / 10 ** (counter - 1)
    print('Формат плавающей точки: x =', number, '* 10 **', counter - 1)

number = int(input('Введите число: '))
floatnum(number)