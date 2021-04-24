def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False


participants = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']

for index in range(len(participants)):
    if not isEven(index):
        print(participants[index])

