file_path = input('Путь к файлу: ').lower()
drive_check = input('На каком диске должен лежать файл: ').lower()
file_extension = input('Требуемое расширение файла: ').lower()

if not file_path.startswith('c'):
    print('\nНеправильно указан диск.')
elif not file_path.endswith('.txt'):
    print('\nНеправильно указано расширение файла.')
else:
    print('\nПуть корректен!')
