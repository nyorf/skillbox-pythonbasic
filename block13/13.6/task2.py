def maxnum(check1, check2):
    return (check1 + check2 + abs(check1 - check2)) // 2

def threenumcheck(num1, num2, num3):
    firstcheck = maxnum(num1, num2)
    secondcheck = maxnum(num2, num3)
    return maxnum(firstcheck, secondcheck)

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))
threenumcheck(num1, num2, num3)