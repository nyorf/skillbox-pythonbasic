# Задача 1. Космическая еда
# Ваш космический корабль потерпел крушение на пустынной планете. Еда здесь не растёт, но вы спасли из обломков
# 100-килограммовый мешок гречки. Из прошлого опыта вы знаете, что если будете экономно питаться, то у вас будет
# уходить по 4 килограмма гречки в месяц. Чтобы прикинуть гречневый бюджет, вы решили написать программу,
# которая выведет информацию о том сколько килограммов гречки у вас должно быть в запасе через месяц,
# два и так далее, пока она не закончится. Используйте цикл for.
bag = 100
month = 0
for supplies in range(bag - 4, -1, -4):
    month += 1
    print('Месяц', month)
    print('Ушло 4 килограмма гречки.')
    print('Осталось:', supplies)
    print()
print('Вся гречка кончится за', month, 'месяцев')