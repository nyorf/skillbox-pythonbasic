import math

def gcd(num1, num2):
    print('Наибольший общий делитель чисел', num1, 'и', num2, '=', math.gcd(num1, num2))

num1 = int(input('Введите число 1: '))
num2 = int(input('Введите число 2: '))
gcd(num1, num2)