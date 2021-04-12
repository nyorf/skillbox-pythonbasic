def locationcheck(x, y, radius):
    if abs(x) <= radius or abs(y) <= radius:
        return True
    else:
        return False


print('Введите координаты монетки:\n')
x = float(input('X: '))
y = float(input('Y: '))
radius = float(input('Введите радиус: '))

if locationcheck(x, y, radius):
    print('\nМонетка где-то рядом!')
else:
    print('\nМонетки в области нет.')