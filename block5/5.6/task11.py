eq_num1 = int(input('Введите первое число: '))
eq_num2 = int(input('Введите второе число: '))
eq_num3 = int(input('Введите третье число: '))
if eq_num1 == eq_num2 == eq_num3:
    print(3)
elif (eq_num1 == eq_num2) or (eq_num1 == eq_num3) or (eq_num2 == eq_num3):
    print(2)
else:
    print(0)