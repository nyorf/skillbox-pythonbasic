def dataRequest(n, k):
    credtior = int(input('Кому: '))
    if not 0 < credtior <= n:
        print('Число не может быть <= 0 или быть больше кол-ва друзей\nПопробуйте ввести данные снова:\n')
        dataRequest(n, k)
    borrower = int(input('От кого: '))
    if not 0 < borrower <= n:
        print('Число не может быть <= 0 или быть больше кол-ва друзей\nПопробуйте ввести данные снова:\n')
        dataRequest(n, k)
    elif borrower == credtior:
        print('Друг не может занять деньги у самого себя.\nПопробуйте ввести данные снова:\n')
        dataRequest(n, k)
    amount = int(input('Сколько: '))
    if amount < 0:
        print('Число не может быть отрицательным.\nПопробуйте ввести данные снова:\n')
        dataRequest(n, k)
    return credtior, borrower, amount
        

n = 2 #int(input('Введите количество друзей: '))
k = 3 #int(input('Введите количество долговых расписок: '))
friends = []

for _ in range(n):
    friends.append([0])

print(friends)

for debt in range(1, k + 1):
    print('\n' + str(debt), 'расписка')
    creditor, borrower, amount = dataRequest(n, k)
    friends[creditor - 1][0] += amount
    friends[borrower - 1][0] -= amount

print('\nБаланс друзей: ')
for friend in range(1, n + 1):
    print(str(friend) + ':', friends[friend - 1][0])
