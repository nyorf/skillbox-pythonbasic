from random import randint

n = int(input('Введите количество элементов списка: '))
number_a = randint(0, (n // 2) - 1)
number_b = randint(n // 2, n)
array = [randint(1, 100) for _ in range(n)]

print('A =', str(number_a) + ';', 'B =', str(number_b))
print('Список:', array)
array[number_a:number_b + 1] = []
print('Обновлённый список:', array)
