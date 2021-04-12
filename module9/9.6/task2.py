carambaCounter = 0
for pirate in range(10):
    reply = input('Пират, крикни что-нибудь! ')
    if (reply == 'Карамба') or (reply == 'карамба'):
        carambaCounter += 1
print('Всего', carambaCounter, 'пиратов крикнули "Карамба".')