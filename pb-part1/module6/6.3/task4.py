balance = int(input('Введите стартовую сумму: '))
while balance < 10000:
    dice_num = int(input('Сколько выпало на кубике? '))
    if dice_num == 3:
        print('Вы проиграли всё!')
        balance = 0
        break
    else:
        balance += 500
        print('Вы выиграли 500 рублей!')
print('Игра окончена!')
print('Ваш баланс:', str(balance) + '₽')