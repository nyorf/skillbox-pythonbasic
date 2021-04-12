def bedroom():
    print('\nВы в спальне. Куда идём?')
    print('\n1. В ванну')
    print('2. В коридор')
    print('\nВаш выбор:', end=' ')
    choice = int(input())
    if choice == 1:
        bathroom()
    elif choice == 2:
        corridor()
    else:
        print('Ошибка ввода. Попробуйте снова.')
        bedroom()

def corridor():
    print('\nВы в коридоре. Куда идём?')
    print('\n1. В спальню')
    print('2. В ванну')
    print('3. На кухню')
    print('4. В дверь')
    print('\nВаш выбор:', end=' ')
    choice = int(input())
    if choice == 1:
        bedroom()
    elif choice == 2:
        bathroom()
    elif choice == 3:
        kitchen()
    elif choice == 4:
        gameover(1)
    else:
        print('Ошибка ввода. Попробуйте снова.')
        corridor()

def bathroom():
    print('\nВы в ванне. Куда идём?')
    print('\n1. В коридор')
    print('2. В спальню')
    print('\nВаш выбор:', end=' ')
    choice = int(input())
    if choice == 1:
        corridor()
    elif choice == 2:
        bedroom()
    else:
        print('Ошибка ввода. Попробуйте снова.')
        bathroom()

def kitchen():
    print('\nВы на кухне. Куда идём?')
    print('\n1. В коридор')
    print('2. В окно')
    print('\nВаш выбор:', end=' ')
    choice = int(input())
    if choice == 1:
        corridor()
    elif choice == 2:
        gameover(0)
    else:
        print('Ошибка ввода. Попробуйте снова.')
        kitchen()

def gameover(result):
    if result == 1:
        print('Вы вышли из квартиры! Игра окончена.')
    elif result == 0:
        print('Вы погибли. Игра окончена.')

bedroom()