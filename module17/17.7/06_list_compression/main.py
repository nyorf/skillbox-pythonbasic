from random import randint

n = int(input('Количество чисел в списке: '))
original_array = [randint(0, 2) for _ in range(n)]

print('Список до сжатия:', original_array)

compressed_array_zeros = [elem for elem in original_array if elem != 0]
compressed_array_zeros.extend([elem for elem in original_array if elem == 0])

print('Список с нулями:', compressed_array_zeros)

compressed_array = [elem for elem in compressed_array_zeros if elem != 0]

print('Список после сжатия:', compressed_array)

# пока не догадываюсь как более эффективно это реализовать
# только через list comprehensions :(
