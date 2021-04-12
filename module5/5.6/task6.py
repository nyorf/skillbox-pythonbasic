clients = int(input('Сколько клиентов? '))
cashiers = int(input('А продавцов? '))
c_salary = int(input('А какая зарплата у продавцов? '))
if clients < 0 or cashiers < 0 or c_salary < 0:
    exit('Введённые вами числа должны быть больше нуля!')
else:
    if clients / cashiers > 4:
        print('Слишком мало продавцов!')
        if c_salary < 20000:
            c_salary += 2000
    else:
        print('Продавцов достаточно.')
    print('Текущая зарплата у продавцов:', str(c_salary) + '₽')