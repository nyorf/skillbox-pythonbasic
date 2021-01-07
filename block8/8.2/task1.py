lastNum = int(input('До какого числа нужно получить кубы? '))
for num in range(1, lastNum // 2 + 1):
    num *= 2
    print('Куб числа', num, '=', num ** 3)
