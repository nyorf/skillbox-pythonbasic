nums_list = []

num_count = int(input('Количество чисел в списке: '))
for _ in range(num_count):
    num = int(input('Введите число: '))
    nums_list.append(num)

print('Максимальное число в списке:', max(nums_list))
print('Минимальное число в списке:', min(nums_list))
