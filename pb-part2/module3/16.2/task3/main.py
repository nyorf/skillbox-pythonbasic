films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня',
         'Проклятый остров', 'Начало', 'Матрица']

usrtop = []

while True:
    print('\nВаш текущий топ фильмов:', usrtop)
    usrinput = input('\nВведите название фильма: ')
    print('Команды: добавить, вставить, удалить')
    usrcmd = input('Введите команду: ')
    if usrinput in films:
        if usrcmd == 'добавить' and not usrinput in usrtop:
            usrtop.append(usrinput)
        elif usrcmd == 'вставить' and not usrinput in usrtop:
            if len(usrtop) == 0:
                print('Ваш топ фильмов на данный момент пустой. Добавьте'
                      ' что-нибудь в него с помощью команды "добавить".')
            else:
                print('Ваш текущий топ фильмов:')
                for i in range(len(usrtop)):
                    print(str(i + 1) + ')', usrtop[i])
                insertpos = int(input('\nНа какую позицию вставить фильм? ')) - 1
                usrtop.insert(insertpos, usrinput)
        elif usrcmd == 'удалить' and usrinput in usrtop:
            usrtop.remove(usrinput)
        elif usrcmd == 'добавить' and usrinput in usrtop:
            print('Этот фильм уже есть в вашем топе.')
        elif usrcmd == 'вставить' and usrinput in usrtop:
            print('Этот фильм уже есть в вашем топе.')
        elif usrcmd == 'удалить' and not usrinput in usrtop:
            print('Этого фильма нет в вашем топе. Удалять нечего.')
    else:
        print('Этого фильма нет на нашем сайте.')
