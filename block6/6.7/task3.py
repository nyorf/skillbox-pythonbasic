debtor_name = input('Введите своё имя: ')
debt = int(input('Сколько вы сейчас должны? '))
while debt > 0:
    print(debtor_name + ', ваша задолженность составляет', str(debt) + '₽')
    payment = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? '))
    debt -= payment
    if debt > 0:
        print('Маловато', debtor_name + '. Давайте ещё раз.')
print('Отлично,', debtor_name + '! Вы погасили долг. Спасибо!')