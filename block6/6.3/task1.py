weather = int(input('Сколько на улице градусов? '))
meters = 0
while weather >= 15:
    meters += 20
    weather -= 2
    if weather <= 15:
        break
    meters += 10
print('Погода испортилась, пора уходить!')
print('Вы прошли', meters, 'метров')