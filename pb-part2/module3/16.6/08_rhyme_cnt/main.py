playersCount = int(input('Введите количество человек: '))
eliminatedOnNumber = int(input('Какое число в считалке? '))
players = list(range(1, playersCount + 1))
firstPlayer = 0
print('Значит, выбывает каждый', eliminatedOnNumber, 'человек.')

while len(players) > 1:
    print('\nТекущий круг людей:', players)
    print('Начало счёта с номера', players[firstPlayer])
    removedIndex = (firstPlayer + eliminatedOnNumber) % len(players) - 1
    if removedIndex == -1:
        print('Выбывает человек под номером:', players[len(players) - 1])
        firstPlayer = 0
    else:
        print('Выбывает человек под номером:', players[removedIndex])
        firstPlayer = removedIndex
    players.pop(removedIndex)

print('\nОстался человек под номером', players[0])
