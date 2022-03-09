number_a = int(input('Введите число A: '))
number_b = int(input('Введите число B: '))

even_numbers = [x for x in range(number_a, number_b + 1) if x % 2 == 0]

print('Список чётных чисел от A до B:', even_numbers)
