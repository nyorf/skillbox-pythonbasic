from random import randint

original_prices = [randint(-20, 20) for _ in range(5)]
new_prices = original_prices[:]
lost_profits = 0

for i in range(len(original_prices)):
    if new_prices[i] < 0:
        lost_profits += -new_prices[i]
        new_prices[i] = 0

print('Оригинальный список:', original_prices)
print('Новый список:', new_prices)
print('Мы потеряли:', lost_profits)
