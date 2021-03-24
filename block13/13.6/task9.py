def factorial(number):
    result = 1
    for num in range(1, number + 1):
        result *= num
    return result

def power(number, power):
    if power == 0:
        return 1
    else:
        result = number
        for _ in range(power - 1):
            result *= number
        return result


term = 1
n = 0
result = 0
precision = float(input('Введите точность: '))
x = float(input('Введите x: '))

while abs(term) > precision:
    term = power(-1, n) * (power(x, 2 * n) / factorial(2 * n))
    result += term
    n += 1

print(result)
