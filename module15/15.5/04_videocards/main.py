gpu_count = int(input('Введите количество видеокарт: '))
gpus = []
gpus_redacted = []
topgpu = 0

for gpu in range(gpu_count):
    print(gpu + 1, 'видеокарта:', end=' ')
    gpu_model = int(input())
    gpus.append(gpu_model)
    topgpu = max(topgpu, gpu_model)

print('Старый список видеокарт:', gpus)
for gpu in gpus:
    if gpu != topgpu:
        gpus_redacted.append(gpu)

print('Новый список видеокарт:', gpus_redacted)
