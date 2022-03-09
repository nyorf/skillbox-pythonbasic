from traceback import print_tb


original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]

fixed_prices = [price if price > 0 else 0 for price in original_prices]

print('Старые цены:', original_prices)
print('Исправленные цены:', fixed_prices)
