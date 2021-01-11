# Задача 9. Выражение
# Дано число x. Напишите программу для вычисления следующего выражения (см. в задании)
x = int(input('Введите число X: '))
totalNumerator = 1
totalDenominator = 1
for numPower in range(1, 7):
    totalNumerator *= (x - ((2 ** numPower) - 1))
    totalDenominator *= (x - (2 ** numPower))
result = totalNumerator / totalDenominator
print('Ответ:', result)
