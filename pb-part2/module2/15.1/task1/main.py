numbers = [3,7,5]

while True:
    new_number = int(input('Новое число: '))
    numbers.append(new_number)
    print('Текущий список чисел:', numbers)
    for num in numbers:
        print(num ** 2, num ** 3, num ** 4)
    print()