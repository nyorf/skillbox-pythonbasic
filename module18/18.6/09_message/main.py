def reverse(text):
    array = list(text)
    array.reverse()
    return ''.join(array)

def encrypt(message):
    encrypted_message = ''
    buffer = ''
    for sym in message:
        if sym.isalpha():
            buffer += sym
        elif not sym.isalpha():
            encrypted_message += reverse(buffer)
            encrypted_message += sym
            buffer = ''
    
    return encrypted_message


message = input('Введите сообщение: ')
print('Новое сообщение: {}'.format(encrypt(message)))


