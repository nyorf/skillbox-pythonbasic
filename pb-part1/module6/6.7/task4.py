# Задача 4. Календари
# Ваня увлекается историей, а в особенности календарями. Он изучает календари разных времён, эпох и народностей
# и для его исследования ему нужно посчитать у кого сколько было месяцев с чётным количеством дней.
# Напишите программу, которая считает количество только четных чисел в последовательности
# (последовательность заканчивается при вводе нуля) и выводит ответ на экран.
month_num = int(input('Введите номер месяца: '))
counter = 0
while month_num != 0:
    if month_num % 2 == 0 and month_num > 0:
        counter += 1
    month_num = int(input('Введите номер следующего месяца (или 0 чтобы завершить программу): '))
print('Всего чётных месяцев:', counter)