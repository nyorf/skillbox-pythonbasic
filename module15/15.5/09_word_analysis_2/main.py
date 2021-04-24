word = list(input('Введите слово: '))
word_reversed = []

for sym in word:
    word_reversed.insert(0, sym)

if word == word_reversed:
    print('Слово является палиндромом.')
else:
    print('Слово не является палиндромом.')
