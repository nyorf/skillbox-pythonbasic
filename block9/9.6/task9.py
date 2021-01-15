string = input('Введите строку: ')
litres = 0
totalLitres = 0
for sym in string:
    litres += 2
    if sym == 'a':
        totalLitres += litres
print('Всего будет произведено', totalLitres, 'литров молока')