from random import randint

n = int(input('Введите длину списка: '))
numbers = [1 if i % 2 == 0 else i % 5 for i in range(n)]

print('Результат:', numbers)
