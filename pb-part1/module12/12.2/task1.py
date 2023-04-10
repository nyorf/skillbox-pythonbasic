def greeting():
    print('\nПривет!')
    print('Добро пожаловать!')

while True:
    a = input('Зайдёте? Да / Нет: ')
    if a == 'Да' or a == 'да':
        greeting()
        print('\nСледующий!')
    elif a == 'Нет' or a == 'нет':
        print('\nСледующий!')