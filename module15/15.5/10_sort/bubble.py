from random import randint

# usrlist = [1, 4, -3, 0, 10]
usrlist = []
for _ in range(20):
    usrlist.append(randint(-100, 100))

print('Изначальный список:', usrlist)

listlength = len(usrlist)
for iteration in range(listlength - 1):
    for listitem in range(listlength - iteration - 1):
        if usrlist[listitem] > usrlist[listitem + 1]:
            usrlist[listitem], usrlist[listitem + 1] = usrlist[listitem + 1], usrlist[listitem]

print('Отсортированный список:', usrlist)