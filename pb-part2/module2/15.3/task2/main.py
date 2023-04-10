usrinput = list(input('Введите строку: '))
reqsymnum = int(input('Введите номер символа: ')) - 1
hasRightNeighbor = True
hasLeftNeighbor = True
if 0 < reqsymnum - 1 < len(usrinput):
    print('Символ слева:', usrinput[reqsymnum - 1])
else:
    print('Символ слева отсутствует.')
    hasLeftNeighbor = False
if 0 < reqsymnum + 1 < len(usrinput):
    print('Символ справа:', usrinput[reqsymnum + 1])
else:
    print('Символ справа отсуствует.')
    hasRightNeighbor = False

if (hasLeftNeighbor and hasRightNeighbor) \
        and usrinput[reqsymnum - 1] == usrinput[reqsymnum] and usrinput[reqsymnum + 1] == usrinput[reqsymnum]:
    print('Рядом есть два таких же символа.')
elif (hasLeftNeighbor and usrinput[reqsymnum - 1] == usrinput[reqsymnum]) \
        or (hasRightNeighbor and usrinput[reqsymnum + 1] == usrinput[reqsymnum]):
    print('Рядом есть ровно один такой же символ.')
else:
    print('Рядом таких же символов нет.')