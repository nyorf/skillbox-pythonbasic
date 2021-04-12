rating = int(input('Что получил по математике? '))
if rating < 2 or rating > 5:
    exit('Введите оценку от 2 до 5.')
else:
    if rating >= 2 and rating <= 3:
        print('Плохо. Марш учиться!')
    else:
        print('Молодец! Можешь отдохнуть.')
