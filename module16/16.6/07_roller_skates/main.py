rollerskates = []
people = []
totalRollerskates = int(input('Введите количество роликов: '))
totalRiders = 0

for i_rs in range(1, totalRollerskates + 1):
    print('Размер', i_rs, 'пары:', end=' ')
    rollerskates.append(int(input()))

totalPeople = int(input('\nВведите количество людей: '))
for i_person in range(1, totalPeople + 1):
    print('Размер ноги', i_person, 'человека:', end=' ')
    people.append(int(input()))

for person in people:
    for pair in rollerskates:
        if person <= pair:
            totalRiders += 1
            rollerskates.remove(pair)
            break

print('Наибольшее количество людей, которые могут взять ролики:', totalRiders)