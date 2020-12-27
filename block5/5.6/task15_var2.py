hour = int(input('Введите текущий час (0-23): '))
if (0 <= hour < 8) or (22 <= hour) or (14 <= hour < 15) or (10 <= hour < 12) or (18 <= hour < 20) or (hour < 0):
    print('Посылку получить нельзя.')
else:
    print('Можно получить посылку.')