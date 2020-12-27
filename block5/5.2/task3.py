money = int(input('Сколько у вас денег? '))
cheese = 60
icecream = 20
if money >= cheese:
    print('На сыр денег хватило')
    money -= cheese
    if money >= icecream:
        print('И на мороженое тоже!')
        money -= icecream
    else:
        print('На мороженое денег не хватает')
else:
    print('Денег маловато.')
print('Осталось', str(money) + '₽')