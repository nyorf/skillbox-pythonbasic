from random import randint

n = int(input('Количество чисел в списке: '))
original_array = [randint(0, 2) for _ in range(n)]
compressed_array = [num for num in original_array if num > 0]

print('Список до сжатия:', original_array)
print('Список после сжатия:', compressed_array)
