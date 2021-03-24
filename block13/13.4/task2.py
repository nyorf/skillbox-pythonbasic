def isEqual(num1, num2, checknum):
    if round(num1 + num2, 15) == checknum:
        return True
    else:
        return False

num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
expectedsumm = float(input('Введите третье число: '))

print(isEqual(num1, num2, expectedsumm))