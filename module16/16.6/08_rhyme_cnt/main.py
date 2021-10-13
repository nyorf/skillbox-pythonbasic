playersCount = int(input('Введите количество человек: '))
eliminatedOnNumber = int(input('Какое число в считалке? '))
players = list(range(1, playersCount + 1))
lastPlayer = players[0]
print('Значит, выбывает каждый', eliminatedOnNumber, 'человек.')

# :(