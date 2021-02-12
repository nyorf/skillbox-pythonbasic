import math
while True:
    filesize = round(float(input('Введите размер файла для скачивания: ')), 2)
    speed = round(float(input('Введите скорость вашего соединения: ')), 2)
    if speed < 0 or filesize < 0: # контроль входа
         print('Скорость и/или размер файла не могут быть отрицательными!')
    elif filesize.is_integer() and speed.is_integer(): # если filesize и speed - целые, преобразовать в int
        filesize = int(filesize)
        speed = int(speed)
        break
    else:
        break
totalDownloaded = 0
onePercent = filesize / 100
downloadPercentage = 0
seconds = 0
while totalDownloaded < filesize: # основной цикл
    seconds += 1
    totalDownloaded += float(speed)
    if totalDownloaded > filesize: # если "загрузилось" больше размера файла => исправить print
        totalDownloaded = float(filesize)
    downloadPercentage = math.ceil(totalDownloaded / onePercent) # высчет процентов
    if totalDownloaded.is_integer(): # если totalDownloaded - целое, преобразовать в int
        totalDownloaded = int(totalDownloaded)
    else: # если дробное, округлить до 2 чисел после запятой
        totalDownloaded = round(totalDownloaded, 2)
    print('Прошло', seconds, 'секунд. Скачано:', end=' ')
    print(str(totalDownloaded), end='')
    print('mb из', str(filesize) + 'mb', end=' ')
    print('(' + str(downloadPercentage) + '%)')
