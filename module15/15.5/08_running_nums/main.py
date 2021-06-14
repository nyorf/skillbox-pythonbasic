usrlist = [1, 2, 3, 4, 5]
movefor = int(input('Сдвиг: '))

print('Изначальный список:', usrlist)

for _ in range(movefor):
    usrlist.insert(0, usrlist[len(usrlist) - 1])
    del usrlist[len(usrlist) - 1]

print('Сдвинутый список:', usrlist)
