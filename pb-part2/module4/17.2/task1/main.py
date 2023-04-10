number_a = int(input('Введите число A: '))
number_b = int(input('Введите число B: '))

cubes = [x ** 3 for x in range(number_a, number_b + 1)]
squares = [x ** 2 for x in range(number_a, number_b + 1)]

print('\nСписок кубов чисел в диапазоне от', number_a, 'до', number_b, '=', cubes)
print('Список квадратов чисел в диапазоне от', number_a, 'до', number_b, '=', squares)
