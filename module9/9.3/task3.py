text = input('Введите текст: ')
smallCount = 0
largeCount = 0

for sym in text:
    if sym == 'Ы':
        largeCount += 1
    elif sym == 'ы':
        smallCount += 1

print('Всего маленьких "ы":', smallCount)
print('Всего больших "Ы":', largeCount)