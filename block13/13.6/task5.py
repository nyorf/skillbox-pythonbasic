import math

precision = float(input('Введите точность: '))

term = 1
denominator = 0
result = 0

while term > precision:
    term = 1 / math.factorial(denominator)
    result += term
    denominator += 1

print('Результат:', result)