def floatreverse(number):
    intpart = ''
    isIntPart = True
    floatpart = ''
    isFloatPart = False
    for sym in str(number):
        if sym == '.':
            isIntPart = False
            isFloatPart = True
        elif isIntPart:
            intpart = sym + intpart
        elif isFloatPart:
            floatpart = sym + floatpart
    return float(intpart + '.' + floatpart)


firstnumber = float(input('Введите первое число: '))
reversedFirstNumber = floatreverse(firstnumber)
secondnumber = float(input('Введите второе число: '))
reversedSecondNumber = floatreverse(secondnumber)

print('\nПервое число наоборот:', reversedFirstNumber)
print('Второе число наоборот:', reversedSecondNumber)
print('Сумма:', reversedFirstNumber + reversedSecondNumber)