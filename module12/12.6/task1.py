def summa_n(num):
    summary = 0
    for i in range(1, num + 1):
        summary += i
    print('Я знаю, что сумма чисел от 1 до', num, 'равна', summary)

summa_n(int(input('Введите число: ')))