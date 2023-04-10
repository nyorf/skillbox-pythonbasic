def forbidden_chars(string):
    chars = '@№$%^&*()'
    for sym in chars:
        if string.startswith(sym):
            return True

    return False


def allowed_exts(string):
    extenstions = ['.docx', '.txt']
    for ext in extenstions:
        if string.endswith(ext):
            return True

    return False


file_name = input('Введите название файла: ')

if forbidden_chars(file_name):
    print('\nОшибка: название начинается на один из специальных символов.')
elif not allowed_exts(file_name):
    print('\nОшибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('\nФайл назван верно.')

# зачёт!
