hours = int(input('Сколько часов длится эксперимент? '))
cells = 1
for hour in range(1, hours // 3 + 1):
    print('Прошло часов:', hour * 3)
    cells *= 2
    print('Клеток:', cells)
    print('Прошло часов:', hour * 3)
    remainingHours = hours - hour * 3
    print('Часов до конца эксперимента:', remainingHours)
    print()