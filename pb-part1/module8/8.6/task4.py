# Задача 4.
# Напишите программу, которая считывает с клавиатуры два числа a и b, считает и выводит на консоль
# среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу c.
a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число с: '))
avg = 0
correctNums = 0
for number in range(a, b + 1):
    if number % c == 0:
        avg += number
        correctNums += 1
print(avg / correctNums)