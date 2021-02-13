import math
while True:
    filesize = int(input('Введите размер файла для скачивания: '))
    speed = int(input('Введите скорость вашего соединения: '))
    if speed < 0 or filesize < 0: # контроль входа
         print('Скорость и/или размер файла не могут быть отрицательными!')
    else:
        break
totalDownloaded = 0
onePercent = filesize / 100
downloadPercentage = 0
seconds = 0
while totalDownloaded < filesize: # основной цикл
    seconds += 1
    totalDownloaded += speed
    if totalDownloaded > filesize: # если "загрузилось" больше размера файла => исправить print
        totalDownloaded = filesize
    downloadPercentage = math.ceil(totalDownloaded / onePercent) # высчет процентов
    print('Прошло', seconds, 'секунд. Скачано:', end=' ')
    print(str(totalDownloaded), end='')
    print('mb из', str(filesize) + 'mb', end=' ')
    print('(' + str(downloadPercentage) + '%)')
