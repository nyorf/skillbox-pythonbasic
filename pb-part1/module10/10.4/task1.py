queue = 5 #int(input('Сколько человек в очереди? '))
for hour in range(1, queue + 1):
    print('Идет час', str(hour) + ':')
    for person in range(hour, queue + 1):
        print('Номер в очереди:', person)
    print()
print('Очередь закончилась.')