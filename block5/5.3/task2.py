income = int(input('Введите ваш доход: '))
if income <= 0:
    exit('Доход не может быть отрицательным.')
else:
    if income < 10000:
        tax = income * 0.13
        print('Ваш налог - 13%')
        print('Сумма вашего налога:', str(tax) + '₽')
    elif income < 50000:
        tax = income * 0.20
        print('Ваш налог - 20%')
        print('Сумма вашего налога:', str(tax) + '₽')
    else:
        tax = income * 0.30
        print('Ваш налог - 30%')
        print('Сумма вашего налога:', str(tax) + '₽')