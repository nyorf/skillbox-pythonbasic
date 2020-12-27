graph_num = int(input('Введите число: '))
if (graph_num >= 10 and graph_num <= 99) or (graph_num <= -10 and graph_num >=-99):
    print('Введённое вами число подходит под нужный диапазон чисел!')
else:
    exit('Введённое вами число не подходит под нужный диапазон чисел!')