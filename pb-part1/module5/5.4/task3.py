temp = int(input('Введите температуру: '))
if temp < 0 or temp > 100:
    print('Температура в среде вышла за рамки промежутка!')
else:
    print('Температура в среде находится в пределах нормы.')