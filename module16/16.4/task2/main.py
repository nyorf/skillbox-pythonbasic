totalMembers = int(input('Введите количество участников: '))
teamMembers = int(input('Введите количество человек в команде: '))
teams = []
num = 1
if totalMembers % teamMembers == 0:
    for _ in range(totalMembers // teamMembers):
        teams.append(list(range(num, num + teamMembers)))
        num += teamMembers
    print('Общий список команд:', teams)
else:
    print(totalMembers, 'участников невозможно поделить на команды по', teamMembers, 'человек!')