seconds = int(input('Сколько секунд ждать? '))
while seconds > 0:
    print(seconds)
    if seconds == 0:
        break
    seconds -= 1