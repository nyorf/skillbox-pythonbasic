# TODO: fix later

def gcd(a, b):
    num1 = max(a, b)
    num2 = min(a, b)
    i = 0
    while True:
        i = num1 % num2
        if i == 0:
            break
        num1 = num2
        num2 = num2 % i
        num1 = i
    return num2

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
print('НОД =', gcd(num1, num2))