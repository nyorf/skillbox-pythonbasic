# Задача 8. Сумма ряда
# Дано натуральное число N. Напишите программу для вычисления следующей суммы ряда (начиная с единицы)
# (см. ряд в задании)
number = int(input('Введите число: '))
total = 0
for power in range(1, number):
    n = 2 ** power
    formulae = ((-1) ** power) * (1 / 2 ** power)
    total += formulae
print(total)