# Задача 8.Замечательные числа
# Напишите программу, которая находит и выводит все двузначные числа, которые равны утроенному произведению своих цифр.
# К таким относятся, например, 15 и 24.
for number in range(10, 100):
    firstDigit = number // 10
    secondDigit = number % 10
    digitM = (firstDigit * secondDigit) * 3
    if number == digitM:
        print(number)