height = int(input('Введите число: '))
leftside = ''
rightside = ''
for line in range(height, 0, -1):
    leftside += str(line)
    rightside = str(line) + rightside
    print(leftside + '.' * (line-1), end='')
    print('.' * (line-1) + rightside)