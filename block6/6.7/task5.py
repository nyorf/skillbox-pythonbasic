month_num = int(input('Введите номер месяца: '))
counter = 0
while month_num != 0:
    month_num = int(input('Введите номер следующего месяца (или 0 чтобы завершить программу): '))
    if month_num % 2 == 0 and month_num > 0:
        counter += 1
print('Всего чётных месяцев:', counter)