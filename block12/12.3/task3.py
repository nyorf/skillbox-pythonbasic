def isPrime(endNum):
    reqCounter = 0
    print('\nПростых чисел в последовательности:', end=' ')
    for num in range(1, endNum + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                reqCounter += 1
    print(reqCounter)

endNum = int(input('Введите количество чисел: '))
isPrime(endNum)