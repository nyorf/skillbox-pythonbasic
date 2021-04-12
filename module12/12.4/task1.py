def rangeavgwithfor(a, b):
    summ = 0
    counter = 0
    for num in range(a, b + 1):
        counter += 1
        summ += num
    print('Среднее арифметическое чисел в промежутке [' + str(a) + '; ' + str(b) + '] = ', summ / counter)

def rangeavg(a, b):
    avg = (a + b) / 2
    print('Среднее арифметическое чисел в промежутке [' + str(a) + '; ' + str(b) + '] = ', avg)

rangeavg(int(input('Введите левую границу: ')), int(input('Введите правую границу: ')))