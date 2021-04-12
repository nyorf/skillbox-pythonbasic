def decision():
    number = int(input('Введите число: '))
    print('\nЧто вы хотите сделать?')
    print('1. - посчитать сумму цифр в числе')
    print('2. - найти самую большую цифру в числе')
    print('3. - найти самую маленькую цифру в числе')
    choice = int(input('\nВаш выбор: '))
    if choice == 1:
        digitsumm(number)
    elif choice == 2:
        maxdigit(number)
    elif choice == 3:
        mindigit(number)
    else:
        print('Ошибка ввода, попробуйте снова.')
        decision()
def digitsumm(num):
    summ = 0
    for digit in str(num):
        summ += int(digit)
    print('Сумма чисел числа', num, 'равна', summ)
def maxdigit(num):
    maxDigit = 0
    for digit in str(num):
        if int(digit) > maxDigit:
            maxDigit = int(digit)
    print('Самая большая цифра в числе', str(num) + ':', maxDigit)
def mindigit(num):
    maxDigit = 10
    for digit in str(num):
        if int(digit) < maxDigit:
            maxDigit = int(digit)
    print('Самая маленькая цифра в числе', str(num) + ':', maxDigit)

decision()