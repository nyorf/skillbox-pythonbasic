machine_count = int(input('Введите количество станков: '))
room_size = int(input('Введите площадь помещения (кв.м): '))
if machine_count >= 5 and room_size >= 100:
    print('Всё отлично, это наш вариант!')
else:
    print('Не подходит. Нужно искать дальше')