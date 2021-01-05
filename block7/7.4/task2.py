num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
summ = 0
for summ_count in range(num1, num2 + 1):
    summ += summ_count
print('Сумма чисел от', num1, 'до', num2, 'равна', summ)