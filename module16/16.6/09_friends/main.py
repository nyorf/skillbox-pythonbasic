n = 2 #int(input('Введите количество друзей: '))
k = 3 #int(input('Введите количество долговых расписок: '))
friends = []

for _ in range(n):
    friends.append(0)
    
for debt in range(1, k + 1):
    print('\n' + str(debt), 'расписка')
    while True:
        creditor = int(input('Кому: '))
        if not 0 < creditor <= n:
            print('Число не может быть <= 0 или быть больше кол-ва друзей\nПопробуйте ввести данные снова:\n')
            continue
        borrower = int(input('От кого: '))
        if not 0 < borrower <= n:
            print('Число не может быть <= 0 или быть больше кол-ва друзей\nПопробуйте ввести данные снова:\n')
            continue
        elif borrower == creditor:
            print('Друг не может занять деньги у самого себя.\nПопробуйте ввести данные снова:\n')
            continue
        amount = int(input('Сколько: '))
        if amount < 0:
            print('Число не может быть отрицательным.\nПопробуйте ввести данные снова:\n')
            continue
        else:
            break
    friends[creditor - 1] += amount
    friends[borrower - 1] -= amount

print('\nБаланс друзей: ')
for friend in range(1, n + 1):
    print(str(friend) + ':', friends[friend - 1])