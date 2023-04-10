alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

message = input('Введите сообщение: ').lower().split()
shift = int(input('Введите сдвиг: '))
encrypted_message = [''.join([alphabet[-(len(alphabet) - alphabet.index(letter) - shift)] 
                        for letter in word]) 
                        for word in message]

print()

output = ' '.join(encrypted_message)
print('Зашифрованное сообщение:', output)
