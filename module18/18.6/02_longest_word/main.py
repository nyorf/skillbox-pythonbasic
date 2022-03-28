string = input('Введите строку: ').split()
longest_word = ''

for word in string:
    if len(word) > len(longest_word):
        longest_word = word
    elif len(word) == len(longest_word):
        continue

print('Самое длинное слово:', longest_word)
print('Длина этого слова:', len(longest_word))
