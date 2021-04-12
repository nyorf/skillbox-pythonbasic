balance = int(input('Сколько денег на карте? '))
while balance > 3000:
    purchase = int(input('Сколько стоила покупка: '))
    balance -= purchase
    print('Ещё можно совершить покупок на', str(balance - 3000) + '₽')
print('Внимание: на карте осталось мало денег! Остановитесь!')
print('На карте осталось:', str(balance) + '₽')