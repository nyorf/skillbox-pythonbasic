totalNumbers = int(input('Сколько всего чисел будет введено? '))
currentNum = 1
maxSumm = 0
reqNum = 0
for number in range(1, totalNumbers + 1):
    digitSumm = 0
    print('Введите', str(number) + '-е число:', end=' ')
    currentNum = int(input())
    workNum = currentNum
    while workNum != 0:
        lastDigit = workNum % 10
        digitSumm += lastDigit
        workNum //= 10
    if digitSumm > maxSumm:
        maxSumm = digitSumm
        reqNum = currentNum
print('Число с наибольшей суммой цифр:', reqNum, end=', ')
print('сумма его цифр:', maxSumm)
