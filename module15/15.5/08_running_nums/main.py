usrlist = [1, 2, 3, 4, 5]
shift = int(input('Сдвиг: '))

print('Изначальный список:', usrlist)

length = len(usrlist)

for _ in range(shift):
    lastnum = usrlist[-1]
    for i in range(1, length + 1):
        if i == length:
            usrlist[-i] = lastnum
        else:
            usrlist[-i] = usrlist[-i - 1]

print('Сдвинутый список:', usrlist)
