def maxnum(check1, check2):
    return (check1 + check2 + abs(check1 - check2)) // 2

def threenumcheck(num1, num2, num3):
    if maxnum(num1, num2) < maxnum(num2, num3):
        print('Наибольшее число:', maxnum(num2, num3))
    elif maxnum(num1, num2) > maxnum(num2, num3):
        print('Наибольшее число:', maxnum(num1, num2))
    else:
        print('Введите три разных числа!')

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))
threenumcheck(num1, num2, num3)