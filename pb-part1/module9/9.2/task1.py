badGrades = 0
answer = input('Кто написал произведение "Евгений Онегин"? ')
for pupil in range(5):
    if (answer == 'Пушкин') or (answer == 'пушкин'):
        print('Правильно, молодец!')
        break
    else:
        print('Неправильно, два!')
        badGrades += 1
print('Всего плохих оценок:', badGrades)