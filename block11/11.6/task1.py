costEUR = float(input('Введите стоимость покупки в €: '))
costUSD = costEUR * 1.25
costRUB = costUSD * 60.87
print('Стоимость покупки в ₽:', round(costRUB, 2))