def creditorCheck(n):
    while True:
        creditor = int(input('Кому: '))
        if not 0 < creditor <= n:
            print('Число не может быть <= 0 или быть больше кол-ва друзей\nПопробуйте ввести данные снова:\n')
        else:
            return creditor

def borrowerCheck(n):
    while True:
        borrower = int(input('От кого: '))
        if not 0 < borrower <= n:
            print('Число не может быть <= 0 или быть больше кол-ва друзей\nПопробуйте ввести данные снова:\n')
        elif borrower == creditor:
            print('Друг не может занять деньги у самого себя.\nПопробуйте ввести данные снова:\n')
        else:
            return borrower
        
def amountCheck():
    while True:
        amount = int(input('Сколько: '))
        if amount < 0:
            print('Число не может быть отрицательным.\nПопробуйте ввести данные снова:\n')
        else:
            return amount


n = int(input('Введите количество друзей: '))
k = int(input('Введите количество долговых расписок: '))
friends = []

for _ in range(n):
    friends.append(0)
    
for debt in range(1, k + 1):
    print('\n' + str(debt), 'расписка')
    creditor = creditorCheck(n)
    borrower = borrowerCheck(n)
    amount = amountCheck()
    friends[creditor - 1] += amount
    friends[borrower - 1] -= amount

print('\nБаланс друзей: ')
for friend in range(1, n + 1):
    print(str(friend) + ':', friends[friend - 1])