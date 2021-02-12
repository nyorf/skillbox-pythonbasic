weight = float(input('Введите вес (в кг): '))
height = float(input('Введите рост (в метрах): '))

imt = round(weight / height ** 2)

if imt < 18.5:
    print('У вас недобор веса!')
elif imt < 25:
    print('У вас нормальный вес!')
elif imt < 30:
    print('У вас избыток веса!')
else:
    print('У вас ожирение!')