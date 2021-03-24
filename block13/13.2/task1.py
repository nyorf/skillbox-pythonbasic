def summa_n(number):
    summ = 0
    for i in range(1, number + 1):
        summ += i
    return summ

number = int(input('Введите число: '))
secondnum = summa_n(number)
print('Сумма от 1 до', number, '=', secondnum)
print('Сумма от 1 до', secondnum, '=', summa_n(secondnum))