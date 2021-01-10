# Задача 9. Выражение
# Дано число x. Напишите программу для вычисления следующего выражения (см. в задании)
x = int(input('Введите число X: '))
totalNumerator = 1
totalDenominator = 1
for numUp in range(2, 7):
    numr = 2 * 2 ** (numUp - 1)
    totalNumerator *= (x - numr)
for numDenom in range(2, 7):
    denomr = (2 * 2 ** (numDenom - 1)) - 1
    totalDenominator *= (x - denomr)
result = totalNumerator / totalDenominator
print('Ответ:', result)
