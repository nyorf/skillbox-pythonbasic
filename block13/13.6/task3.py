def numreverse(number):
    reversednum = ''
    for sym in str(number):
        reversednum = sym + reversednum
    return int(reversednum)

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
print('\nПервое число наоборот:', numreverse(num1))
print('Второе число наоборот:', numreverse(num2))
print('Сумма:', num1 + num2)
print('\nСумма наоборот:', numreverse(num1 + num2 ))