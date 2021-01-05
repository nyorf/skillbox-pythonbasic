# Задача 4. С заботой о природе
# Огромный заповедник поделён на большое количество секторов. И у каждого сектора есть номер.
# Мы ответственны за группу секторов с номерами с 30-го по 35-ый и нам нужно следить за тем, чтобы посетителей
# в каждом секторе было меньше 10. А заодно и фиксировать для общей статистики, сколько раз это правило было нарушено.
# Напишите программу, которая для каждого сектора запрашивает текущее количество людей в нём, и если оно больше 10,
# то фиксирует нарушение. В конце выведите количество нарушений
violations = 0
for sector in range(30, 36):
    print(sector, 'сектор')
    visitors = int(input('Сколько людей в данном секторе? '))
    if visitors <= 10:
        print('Всё спокойно.')
    else:
        print('Нарушение! Слишком много людей в секторе!')
        violations += 1
print('Количество нарушений', violations)