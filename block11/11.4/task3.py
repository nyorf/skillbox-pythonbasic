import math

number = float(input('Введите число: '))

print('Округление числа вниз:', math.floor(number))
print('Округление числа вверх:', math.ceil(number))
print('Модуль числа', number, '= |' + str(abs(number)) + '|')
print('Квадратный корень из числа', number, '=', math.sqrt(number))
print('Экспонента, умноженная на число', str(number) + ':', math.exp(number))
print('Натуральный логарифм числа', str(number) + ':', math.log(number, math.e))
print('Логарифм числа', number, 'по основанию 2:', math.log2(number))
print('Логарифм числа', number, 'по основанию 10:', math.log10(number))
print('Синус числа', number, '=', str(math.sin(number)) + '; косинус числа', number, '=', math.cos(number))

if math.ceil(number) == math.floor(number):
    number = int(number)
    print('Факториал числа', number, '=', math.factorial(number))
