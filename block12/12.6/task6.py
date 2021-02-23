def coinsearch(x, y):
    if -1 <= x <= 1 and -1 <= y <= 1:
        print('Монетка где-то рядом.')
    else:
        print('Монетки в области нет.')

x = float(input('Введите координату x: '))
y = float(input('Введите координату y: '))
coinsearch(x, y)