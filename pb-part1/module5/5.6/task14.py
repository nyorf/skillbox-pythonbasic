income = int(input('Введите ваш доход: '))
if income < 0:
    exit('Доход не может быть отрицательным!')
else:
    if income <= 10000:
        tax = income * 0.13
    elif 10000 < income <= 50000:
        tax = (10000 * 0.13) + ((income - 10000) * 0.20)
    else:
        tax = (10000 * 0.13) + ((50000 - 10000) * 0.20) + ((income - 50000) * 0.30)
print('Сумма вашего налога составила:', str(tax) + '₽')

