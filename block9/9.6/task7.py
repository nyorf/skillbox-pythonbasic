text = input('Введите текст: ')
letterCounter = 0
longestWord = 0
for letter in text:
    if letter == ' ':
        if longestWord < letterCounter:
            longestWord = letterCounter
        letterCounter = 0
    else:
        letterCounter += 1
print('Длина самого длинного слова:', longestWord)
