cells_count = int(input('Введите количество клеток: '))
cells = []

for cell_index in range(1, cells_count + 1):
    print('Эффективность', cell_index, 'клетки:', end=' ')
    cell_efficiency = int(input())
    cells.append(cell_efficiency)

print('\nНеподходящие значения:', end=' ')
current_index = -1
for cell in cells:
    current_index += 1
    if cells[current_index] < current_index:
        print(cells[current_index], end='; ')

