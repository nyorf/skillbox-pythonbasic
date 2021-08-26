playersCount = 5 #int(input('Введите количество человек: '))
players = list(range(1, playersCount + 1))
eliminateAtCount = 7 #int(input('Введите число в считалке: '))
print('Значит, выбывает каждый', eliminateAtCount, 'человек')
startingPlayer = 0 # индекс начального игрока
currentIndex = 0
