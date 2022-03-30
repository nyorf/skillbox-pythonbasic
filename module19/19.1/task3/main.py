contacts = {}

while True:
    print('\nТекущие контакты на телефоне:\n')
    if len(contacts) == 0:
        print('<Пусто>')
    else:
        for key in contacts:
            print('{name}: {number}'.format(name = key, number = contacts[key]))
    
    new_name = input('\nВведите имя: ')
    new_number = input('Введите номер телефона: ')

    if new_name in contacts:
        print('\nОшибка: контакт "{}" уже существует.'.format(new_name))
    else:
        contacts[new_name] = new_number
