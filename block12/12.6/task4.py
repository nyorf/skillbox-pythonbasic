def numreverse(number):
    reversednum = ''
    for digit in str(number):
        if digit != '0':
            reversednum = digit + reversednum
    print('Число наоборот:', reversednum)

number = int(input('Введите число: '))
numreverse(number)
