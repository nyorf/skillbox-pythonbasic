words = input('Введите три слова через запятую: ').split(', ')
occurences = [0 for _ in range(len(words))]
text = input('Введите текст: ').split()

result = 0
for word_i in range(len(words)):
    for text_word in text:
        if text_word == words[word_i]:
            occurences[word_i] += 1

for i in range(len(words)):
    output = 'Слово {word} встречается в тексте {occurences} раз.'
    print(output.format(word=words[i], occurences=occurences[i]))
