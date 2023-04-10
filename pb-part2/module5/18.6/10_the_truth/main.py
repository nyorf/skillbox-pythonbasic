import string


def decrypt_caesars(text, alphabet=string.ascii_letters):
    decrypted_text = ''.join([alphabet[alphabet.find(letter) - 1] if letter.isalpha() else letter for letter in text])
    return decrypted_text


def remove_shift(word, shift):
    word = list(word)
    for _ in range(shift):
        word.insert(0, word[-1])
        word.pop(-1)

    word = ''.join(word)

    return word


def decrypt_shift(text):
    current_shift = 3
    text = text.split()
    decrypted_text = []
    for word in text:
        decrypted_text.append(remove_shift(word, current_shift))
        if '/' in word:
            current_shift += 1

    decrypted_text = ' '.join(decrypted_text)
    decrypted_text = decrypted_text.replace('/', '\n')

    return decrypted_text


def decrypt_text():
    text = input('Введите текст: ')
    caesars = decrypt_caesars(text)
    shift = decrypt_shift(caesars)

    return shift


print('Расшифрованный текст:\n{}'.format(decrypt_text()))

# зачёт!
