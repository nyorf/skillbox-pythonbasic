string = input('Введите строку: ')
prevSym = ''
longestS = 0
sCount = 0
for sym in string:
    if sym == 's':
        sCount += 1
        if longestS < sCount:
            longestS = sCount
    else:
        sCount = 0
print('Самая длинная последовательность:', longestS)