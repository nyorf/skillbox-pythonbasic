endNum = int(input('Введите последнее число последовательности: '))
reqCounter = 0
print('Простые числа в последовательности:', end=' ')
for num in range(1, endNum + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num, end=' ')
            reqCounter += 1
print('\nКол-во ростых чисел в последовательности:', reqCounter)