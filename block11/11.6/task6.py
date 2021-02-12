lowerborder = int(input('Введите нижнюю границу: '))
upperborder = int(input('Введите вернхнюю границу: '))
step = int(input('Введите шаг: '))
currentCelsius = 0 - step
currentFarenheit = 0
print('C°', end='\t')
print('T°', end='')
while currentCelsius < upperborder:
    print()
    if currentCelsius + step > upperborder:
        currentCelsius = upperborder
    else:
        currentCelsius += step
    print(currentCelsius, end='\t')
    currentFarenheit = int(32 + currentCelsius * 1.8)
    print(currentFarenheit, end='\t')
