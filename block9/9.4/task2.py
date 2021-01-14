number = int(input('Введите первое число: '))
step = int(input('Введите шаг: '))
summ = 0
print('\nIP-address:', end=' ')
for add in range(3):
    print(number, end='.')
    summ += number
    number += step
print(summ)