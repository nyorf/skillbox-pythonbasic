import random

def rock_paper_scissors():
    print('\n==== Камень-ножницы-бумага ====')
    print('Ваш ход (введите [камень], [ножницы] или [бумага]:', end=' ')
    player = input()
    if player == 'камень':
        player = 1
    elif player == 'ножницы':
        player = 2
    elif player == 'бумага':
        player = 3
    else:
        print('Ошибка ввода, попробуйте снова!')
        rock_paper_scissors()
    bot = random.randint(1, 3)
    if bot == 1:
        print('\nКомпьютер кидает камень.')
    elif bot == 2:
        print('\nКомпьютер кидает ножницы.')
    else:
        print('\nКомпьютер кидает бумагу.')
    if player == bot:
        print('Ничья!')
    elif (player == 1 and bot == 2) or (player == 2 and bot == 3) or (player == 3 and bot == 1):
        print('Вы выиграли!')
    else:
        print('Компьютер выиграл!')
    endgamechoice(1)

def guess_the_number():
    number = str(random.randint(1, 100))
    print('\n==== Угадай число ====')
    print('Компьютер загадал число от 1 до 100. Попробуй угадать это число!')
    print('Если ты захочешь завершить игру, напиши [выход]\n')
    guess = ''
    tries = 0
    while guess != number:
        tries += 1
        print('Попытка №' + str(tries) + ':', end=' ')
        guess = input()
        if guess == 'выход':
            break
    if guess == 'выход':
        print('\nК сожалению, ты не смог угадать число [' + number + ']. Всего попыток:', tries)
    else:
        print('\nМолодец! Ты угадал число [' + number + ']! Всего попыток:', tries)
    endgamechoice(2)

def endgamechoice(game):
    print('\n1. Сыграть снова')
    print('2. Вернуться в главное меню')
    endgamechoice = int(input('\nВаш выбор: '))
    if endgamechoice == 1:
        if game == 1:
            rock_paper_scissors()
        elif game == 2:
            guess_the_number()
    if endgamechoice == 2:
        mainMenu()
    else:
        print('Ошибка ввода! Возвращаюсь в главное меню...\n')
        mainMenu()

def mainMenu():
    print('Привет! В какую игру ты хочешь сыграть?')
    print('\n1. Камень-ножницы-бумага')
    print('2. Угадай число\n')
    menuchoice = int(input('Твой выбор: '))
    if menuchoice == 1:
        rock_paper_scissors()
    elif menuchoice == 2:
        guess_the_number()
    else:
        print('Ошибка ввода! Попробуй снова :)\n')
        mainMenu()

mainMenu()