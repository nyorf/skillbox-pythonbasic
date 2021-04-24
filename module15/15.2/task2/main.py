numbers_list = []
numbers_count = int(input('Введите количество чисел в списке: '))

for count in range(1, numbers_count + 1):
    print('Введите', count, 'число:', end=' ')
    numbers_list.append(int(input()))

divider = int(input('Введите делитель: '))

index_summ = 0
current_index = -1
for number in numbers_list:
    current_index += 1
    if number % divider == 0:
        print('Индекс числа', str(number) + ':', current_index)
        index_summ += current_index

print('Сумма индексов:', index_summ)