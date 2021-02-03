levels = int(input('Введите количество уровней пирамиды: '))
lastnum = -1
for currentlevel in range(1, levels + 1):
    print()
    print(' ' * (levels - currentlevel), end=' ')
    for nums in range(currentlevel):
        lastnum += 2
        print(lastnum, end=' ')