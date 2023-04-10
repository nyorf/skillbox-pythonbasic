def isBobHere(children_array):
    for i in range(len(children_array)):
        if children_array[i].get('name') == 'Bob':
            return i
    
    return None


family_member = {
    "name": "Jane",
    "surname": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "name": "Alice",
            "age": 6
        },
        {
            "name": "Bob",
            "age": 8
        }
    ]
}

print('Имя {}'.format(family_member['name']))
print('Фамилия: {}'.format(family_member['surname']))
print('Хобби: {}'.format(
    ', '.join(family_member['hobbies'])
))
print('Дети: {}'.format(
    ', '.join([children['name'] for children in family_member['children']])
))

bob_index = isBobHere(family_member['children'])

if bob_index != None:
    surname = family_member['children'][bob_index].get('surname', 'Nosurname')
    print(surname)
else:
    print('\nБоба нету в списке детей.')

