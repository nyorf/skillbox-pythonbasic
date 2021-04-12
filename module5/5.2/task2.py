price = 75000
bank = int(input('Введите баланс вашего счёта: '))
if bank >= price:
    bank -= price
    print('Курс успешно приобретён!')
    if bank < 5000:
        bank += 1000
        print('Сделана скидка.')
else:
    print('Недостаточно средств на счету!')
print('Остаток на счету:', str(bank) + '₽')
print('Хорошего дня!')