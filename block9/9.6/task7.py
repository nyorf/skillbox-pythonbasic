text = input('Введите текст: ') + ' '
letterCount = 0
longestWord = 0
for letter in text:
    if letter == ' ':
        if letterCount > longestWord:
            longestWord = letterCount
        letterCount = 0
    else:
        letterCount += 1
print('Самое длинное слово:', longestWord)