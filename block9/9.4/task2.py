number = int(input('Введите первое число: '))
step = int(input('Введите шаг: '))
summ = 0
for add in range(3):
    print(number, end='.')
    summ += number
    number += step
print('\nIP-address:', summ)