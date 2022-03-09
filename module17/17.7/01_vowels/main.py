vowels = ['а', 'у', 'о', 'ы', 'э', 'я', 'ю', 'ё', 'и', 'е']
message = input('Введите текст: ')

msg_vowels = [letter for letter in message if letter in vowels]

print('Список гласных букв:', msg_vowels)
print('Длина списка:', len(msg_vowels))
