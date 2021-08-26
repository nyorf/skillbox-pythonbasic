main = [1, 5, 3]
extra_a = [1, 5, 1, 5]
extra_b = [1, 3, 1, 5, 3, 3]

main.extend(extra_a)
fives = main.count(5)
while 5 in main:
    main.remove(5)

main.extend(extra_b)
threes = main.count(3)

print('Кол-во цифр 5 при первом объединении:', fives)
print('Кол-во цифр 3 при втором объединении:', threes)
print('Итоговый список:', main)