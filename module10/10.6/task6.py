endNum = int(input('Введите конечное число: '))
facSumm = 0
for num in range(1, endNum + 1):
    currentFactorial = 1
    for i in range(1, num + 1):
        currentFactorial *= i
    facSumm += currentFactorial
print('Сумма факториалов от 1 до', endNum, '=', facSumm)