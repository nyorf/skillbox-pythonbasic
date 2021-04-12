while True:
    lowerborder = int(input('Введите нижнюю границу: '))
    upperborder = int(input('Введите вернхнюю границу: '))
    step = int(input('Введите шаг: '))
    if step < 0 or upperborder < 0 or lowerborder < 0 or lowerborder > upperborder:
        print('Проверьте правильность введённых данных!')
    else:
        break
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
