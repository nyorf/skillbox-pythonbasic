def numRequest(text):
    while True:
        number = int(input(text))
        if number <= 200:
            return number
        else:
            print('Попробуйте снова: число больше 200.')


containersCount = int(input('Введите количество контейнеров: '))
containers = []

for _ in range(containersCount):
    container = numRequest('Введите вес контейнера: ')
    containers.append(container)

newContainer = numRequest('Введите вес нового контейнера: ')


for currentIndex in range(len(containers)):
    if containers[currentIndex] > newContainer > containers[currentIndex + 1]:
        print('\nНомер, куда встанет новый контейнер:', currentIndex + 2)
        break
    elif containers[currentIndex] == newContainer and newContainer > containers[currentIndex + 1]:
        print('\nНомер, куда встанет новый контейнер:', currentIndex + 2)
        break
    elif currentIndex == len(containers) - 1:
        print('\nКонтейнер поставить некуда.')
