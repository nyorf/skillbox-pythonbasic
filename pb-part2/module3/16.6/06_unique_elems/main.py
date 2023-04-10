list_a = []
list_b = []

for i_num in range(1, 4):
    print('Введите', i_num, 'число для первого списка:', end=' ')
    list_a.append(int(input()))
print()
for i_num in range(1, 8):
    print('Введите', i_num, 'число для второго списка:', end=' ')
    list_b.append(int(input()))

list_a.extend(list_b)

for num in list_a:
    for _ in range(list_a.count(num) - 1):
        list_a.remove(num)

print('Новый первый список с уникальными элементами:', list_a)

# зачёт!
