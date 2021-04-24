def isAvailable(inputlist, request):
    for item in inputlist:
        if item == request:
            return True
    return False


movies = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

saved_movies = []

print('Для того, чтобы добавить фильм в избранное, введите его название.')
print('(для выхода из программы наберите "end"\n')
usrinput = ''
while True:
    usrinput = input('Введите название фильма: ')
    if isAvailable(movies, usrinput):
        saved_movies.append(usrinput)
        print('Фильм', usrinput, 'успешно добавлен в избранное!\n')
    elif usrinput == 'end':
        break
    else:
        print('Ошибка: фильм', usrinput, 'не найден в базе данных!\n')

print('\nВаши избранные фильмы:', saved_movies)
