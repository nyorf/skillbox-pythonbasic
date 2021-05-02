word = list(input('Введите слово: '))
word_reversed = []

for symnum in range(1, len(word) + 1):
    word_reversed.append(word[-symnum])

if word == word_reversed:
    print('Слово является палиндромом.')
else:
    print('Слово не является палиндромом.')