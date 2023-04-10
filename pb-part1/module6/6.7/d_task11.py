temperature = int(input('Введите температуру: '))
highesttemp = 0
while temperature != 0:
    temperature = int(input('Введите температуру: '))
    if temperature > highesttemp:
        highesttemp = temperature
print('Наибольшая температура:', highesttemp)