goods = [['яблоки', 50], ['апельсины', 190], ['груши', 100], ['нектарины', 200], ['бананы', 77]]
print('Текущий ассортимент:', goods)

newfruit = input('\nВведите название нового фрукта: ')
newfruitprice = int(input('Введите цену нового фрукта: '))

goods.append([newfruit, newfruitprice])
print('\nНовый ассортимент:', goods)

for product in goods:
    product[1] += product[1] * 0.08

print('\nНовый ассортимент с увел. ценой:', goods)