shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

nameRequest = input('Введите название детали: ')
partCounter = 0
totalPrice = 0

for part in shop:
    if part[0] == nameRequest:
        partCounter += 1
        totalPrice += part[1]

print('Количество деталей:', partCounter)
print('Общая стоимость:', totalPrice)

# зачёт!
