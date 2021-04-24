def highestvalue(usrlist):
    topitem = 0
    for item in usrlist:
        if item > topitem:
            topitem = item
    return topitem


gpu_count = int(input('Введите количество видеокарт: '))
gpus = []
gpus_redacted = []

for gpu in range(gpu_count):
    print(gpu + 1, 'видеокарта:', end=' ')
    gpu_model = int(input())
    gpus.append(gpu_model)

print('Старый список видеокарт:', gpus)
topgpu = highestvalue(gpus)
for gpu in gpus:
    if gpu != topgpu:
        gpus_redacted.append(gpu)

print('Новый список видеокарт:', gpus_redacted)
