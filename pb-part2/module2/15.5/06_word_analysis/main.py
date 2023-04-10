usrinput = input('Введите слово: ')
uniqueLetters = []

for sym in usrinput:
    usageCounter = 0
    for symcheck in usrinput:
        if sym == symcheck:
            usageCounter += 1
    if usageCounter == 1:
        uniqueLetters.append(sym)

print('Количество уникальных букв:', len(uniqueLetters))

# зачёт!
