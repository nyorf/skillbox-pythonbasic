word_list = []
words_usage = []

for word_counter in range(1, 4):
    print('Введите', word_counter, 'слово:', end=' ')
    new_word = input()
    word_list.append(new_word)
    words_usage.append(0)

usrinput = ''
while usrinput != 'end':
    usrinput = input('Введите слово из текста: ')
    if usrinput == word_list[0]:
        words_usage[0] += 1
    elif usrinput == word_list[1]:
        words_usage[1] += 1
    elif usrinput == word_list[2]:
        words_usage[2] += 1

print('\nПодсчёт слов в тексте')
print(word_list[0] + ':', words_usage[0])
print(word_list[1] + ':', words_usage[1])
print(word_list[2] + ':', words_usage[2])