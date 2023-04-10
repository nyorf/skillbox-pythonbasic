headerLength = int(input('Введите длину колонтитула: '))
exclamationCount = int(input('Введите количество восклицательных знаков: '))
totalLength = headerLength - exclamationCount
print('~' * (totalLength // 2), end='')
print('!' * exclamationCount, end='')
print('~' * (totalLength // 2))