numCount = int(input('Сколько чисел будет в последовательности? '))
reqCounter = 0
for num in range(1, numCount + 1):
    print('Введите', str(num) + '-е число:', end=' ')
    number = int(input())
    for digit in range(2, number // 2):
        if (num % digit) == 0:
            break
    else:
        reqCounter += 1
print('Простых чисел в последовательности:', reqCounter)