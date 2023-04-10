n = int(input('Введите целое число: '))

squares = {}

for num in range(1, n + 1):
    squares[num] = num ** 2

print(squares)
