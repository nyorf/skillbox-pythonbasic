text = input('Введите текст: ').lower()
hist = dict()

for letter in text:
    if letter in hist:
        hist[letter] += 1
    else:
        hist[letter] = 1

for key in sorted(hist.keys()):
    print('{key}: {value}'.format(
        key = key,
        value = hist[key]
    ))

print('\nМаксимальная частота: {}'.format(max(hist.values())))
