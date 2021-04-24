def isEfficient(cell_index, cell_efficiency):
    if cell_efficiency < cell_index:
        return False
    else:
        return True


cells_count = int(input('Введите количество клеток: '))
cells = []

for cell_index in range(cells_count):
    print('Эффективность', cell_index + 1, 'клетки:', end=' ')
    cell_efficiency = int(input())
    cells.append(cell_efficiency)

print('\nНеподходящие значения:', end=' ')
current_index = -1
for cell in cells:
    current_index += 1
    if not isEfficient(current_index, cells[current_index]):
        print(cells[current_index], end='; ')

