number = int(input('Введите число: '))
counter = 0
while number != 0:
    counter += 1
    number //= 10
print('Количество цифр:', counter)
