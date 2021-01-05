# Задача 6. Успеваемость в классе
# В классе N человек. Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было.
# Напишите программу, которая получает список оценок - N чисел - и выводит на экран сообщение о том,
# кого сегодня больше: отличников, хорошистов или троечников.
totalPupils = int(input('Сколько учеников было в классе? '))
aCounter = 0
bCounter = 0
cCounter = 0
for pupil in range(0, totalPupils):
    mark = int(input('Введите оценку: '))
    if mark == 3:
        cCounter += 1
    elif mark == 4:
        bCounter += 1
    elif mark == 5:
        aCounter += 1
if aCounter > bCounter and aCounter > cCounter:
    print('Сегодня больше отличников!')
elif bCounter > cCounter:
    print('Сегодня больше хорошистов!')
else:
    print('Сегодня больше троечников!')