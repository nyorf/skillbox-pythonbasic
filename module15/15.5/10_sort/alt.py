from math import inf as infinity
from random import randint

# usrlist = [1, 4, -3, 0, 10]
usrlist = []
for _ in range(20):
    usrlist.append(randint(-100, 100))

print('Изначальный список:', usrlist)

length = len(usrlist)
for index in range(length):
    current_index_min = infinity
    index_to_replace = 0
    for check in range(length):
        if usrlist[check] < current_index_min:
            current_index_min = usrlist[check]
            index_to_replace = check
    usrlist[index_to_replace] = infinity
    usrlist.append(current_index_min)

for _ in range(length):
    usrlist.remove(infinity)

print('Отсортированный список:', usrlist)
