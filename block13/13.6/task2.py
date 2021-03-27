def maxnum(check1, check2):
    return (check1 + check2 + abs(check1 - check2)) // 2

def threenumcheck(num1, num2, num3):
    firstcheck = maxnum(num1, num2)
    secondcheck = maxnum(num2, num3)
    if firstcheck < secondcheck:
        print('Наибольшее число:', secondcheck)
    else:
        print('Наибольшее число:', firstcheck)

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))
threenumcheck(num1, num2, num3)