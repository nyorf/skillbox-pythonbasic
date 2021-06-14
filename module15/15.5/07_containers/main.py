containersCount = int(input('Введите количество контейнеров: '))
containers = []

for _ in range(containersCount):
    while True:
        container = int(input('Введите вес контейнера: '))
        if container > 200:
            print('Попробуйте снова: число больше 200.')
        else:
            break
    containers.append(container)

while True:
    newContainer = int(input('Введите вес нового контейнера: '))
    if newContainer > 200:
        print('Попробуйте снова: число больше 200.')
    else:
        break

currentindex = -1
for containerWeight in containers:
    currentindex += 1
    if containers[currentindex] > newContainer:
        print('Номер, куда встанет новый контейнер:', currentindex + 2)
        break
    elif containers[currentindex] == newContainer == containers[currentindex + 1]:
        print('Номер, куда встанет новый контейнер:', currentindex + 1)
        break
    else:
        print('Контейнер поставить некуда.')
        break
