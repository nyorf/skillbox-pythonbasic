letterSize = int(input('Введите размеры листа с письмом: '))
envelopeWidth = 12
envelopeLength = 12
folds = 0
for size in range(letterSize, 11, -(letterSize // 2)):
    print(size)