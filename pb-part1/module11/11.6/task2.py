import math

totalNumbers = int(input('Введите количество чисел: '))
for count in range(totalNumbers):
    number = float(input('Введите число: '))
    if number > 0: # положительные числа
        number = math.ceil(number)
        requiredOutput = math.log(number)
        print('x =', number, '|', 'ln(' + str(number) + ')', '=', requiredOutput)
    elif number < 0: # отрицательные числа
        number = math.floor(number)
        requiredOutput = math.exp(number)
        print('x =', number, '|', 'exp(' + str(number) + ')', '=', requiredOutput)
    else: # для 0 не указано никаких условий
        print(':)')