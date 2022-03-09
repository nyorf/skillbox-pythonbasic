alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

message = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))
shifted_message = [alphabet[-(len(alphabet) - alphabet.index(letter) - shift)] if not letter == ' ' else ' ' for letter in message]

print('Зашифрованное сообщение:', end=' ')
for l in shifted_message:
    print(l, end='')
