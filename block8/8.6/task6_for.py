letterSize = int(input('Введите размеры листа с письмом: '))
envelopeSize = 12
folds = 0
for size in range(letterSize, envelopeSize-1, -(letterSize // 2)):
    folds += 2
    print(folds)