savings = int(input('Сколько отложить денег? '))
while savings < 500000:
    print('Текущий баланс:', str(savings) + '₽')
    savings += int(input('Сколько ещё отложить денег? '))
print('Кирилл, поздравляю! Ты накопил на машину!')
print('Текущий баланс:', str(savings) + '₽')