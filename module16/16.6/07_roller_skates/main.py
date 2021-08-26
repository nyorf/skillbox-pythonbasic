# в условии задачи ответ: "Наибольшее кол-во людей, которые могут взять ролики: 2",
# что странно, ведь в примере даётся всего лишь одна пара с размером 42, значит один из
# посетителей с размером ноги 42 не сможет взять ролики и пойти кататься одновременно
# с другим посетителем с размером 42.

rollerskates = []
people = []
totalRollerskates = int(input('Введите количество роликов: '))
totalRiders = 0

for i_rs in range(1, totalRollerskates + 1):
    print('Размер', i_rs, 'пары:', end=' ')
    rollerskates.append(int(input())) # чтобы получать ответ как в примере - убрать эту строчку

totalPeople = int(input('\nВведите количество людей: '))
for i_person in range(1, totalPeople + 1):
    print('Размер ноги', i_person, 'человека:', end=' ')
    people.append(int(input()))

for person in people:
    if person in rollerskates:
        totalRiders += 1
        rollerskates.remove(person)
        people.remove(person)

print('Наибольшее количество людей, которые могут взять ролики:', totalRiders)