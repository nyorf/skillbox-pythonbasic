# Задача 5. Счастливый билетик.
# В старину, когда даже в столице билеты в общественном транспорте выдавали контролеры, существовало поверье:
# если на билете сумма первых трех цифр в номере билета равна сумме последних трех, то это к удаче.
# Напишите программу, которая получала бы на входе шестизначный номер билета и выводила,
# счастливый ли это билет или нет. К примеру, билеты 666 666 и 252 135 - счастливые, а 123 456 - нет.
# Нужны ли для решения этой задачи циклы?
ticket = int(input('Введите шестизначный номер билета: '))
firstthree_summ = 0
lastthree_summ = 0
counter = 0
while counter != 3:
    last_num = ticket % 10
    lastthree_summ += last_num
    ticket //= 10
    counter += 1
while ticket != 0:
    last_num = ticket % 10
    firstthree_summ += last_num
    ticket //= 10
    counter += 1
print('Сумма первых трех цифр =', firstthree_summ)
print('Сумма последних трёх цифр =', lastthree_summ)