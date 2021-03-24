def numrequest():
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))
    return num1, num2

def digitcheck(num1, num2):
    if digitcounter(num1) < 3 or digitcounter(num2) < 4:
        print('Проверьте правильность ввода чисел!\n')
        return False
    else:
        return True

def digitcounter(number):
    counter = 0
    for _ in str(number):
        counter += 1
    return counter

def digitswitch(number):
    digitcount = digitcounter(number)
    firstdigit = number // 10 ** (digitcount - 1)
    lastdigit = number % 10
    middledigits = number % 10 ** (digitcount - 1) // 10
    result = lastdigit * 10 ** (digitcount - 1) + middledigits * 10 + firstdigit
    return result

num1, num2 = numrequest()
if digitcheck(num1, num2):
    print('\nИзменённое первое число:', digitswitch(num1))
    print('Изменённое второе число:', digitswitch(num2))
    print('\nСумма чисел:', digitswitch(num1) + digitswitch(num2))