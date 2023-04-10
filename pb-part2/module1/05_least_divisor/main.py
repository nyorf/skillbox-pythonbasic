def spd(number):
    for divider in range(2, number + 1):
        if number % divider == 0:
            return divider


number = int(input('Введите число: '))
print('Наименьший делитель, отличный от единицы:', spd(number))