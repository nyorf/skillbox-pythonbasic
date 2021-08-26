guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('\nСейчас на вечеринке', len(guests), 'человек:', guests)
    action = input('Гость пришёл или ушёл? ')
    if action == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
    else:  
        guest_name = input('Имя гостя: ')
        if action == 'пришёл':
            if len(guests) == 6:
                print('Прости,', guest_name + ', но мест нет.')
            else:
                guests.append(guest_name)
                print('\nПривет,', guest_name + '!')
        elif action == 'ушёл':
            if guest_name in guests:
                guests.remove(guest_name)
                print('\nПока,', guest_name + '!')
            else:
                print('Такого гостя на вечеринке нету, попробуй ещё раз.')
        else:
            print('Неверная команда, попробуй ещё раз.')
