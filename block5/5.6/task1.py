exp = int(input('Введите количество опыта: '))
if exp < 1000:
    lvl = 1
elif exp < 2500:
    lvl = 2
elif exp < 5000:
    lvl = 3
else:
    lvl = 4
print('Ваш уровень:', lvl)