# Задача 7. Отрезок
# Напишите программу, которая считывает с клавиатуры два числа a и b, считает и выводит на консоль
# среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.
startpos = int(input('Введите начало отрезка: '))
endpos = int(input('Введите конец отрезка: '))
reqNum = 0
numCount = 0
for pos in range(startpos, endpos + 1):
    if pos % 3 == 0:
        reqNum += pos
        numCount += 1
avg = reqNum / numCount
print('Среднее арифметическое значение нужных чисел =', avg)