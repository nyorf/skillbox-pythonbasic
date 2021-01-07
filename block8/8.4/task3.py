seconds = int(input('Введите количество секунд: '))
for second in range(seconds // 2, 0, -1):
    second *= 2
    print(second)
print('Я иду искать!')