height = int(input('Введите высоту пирамидки: ')) * 2
for line in range(1, height + 1, 2):
    totalLength = (height - line)
    print(' ' * (totalLength // 2), end='')
    print('#' * line, end='')
    print(' ' * (totalLength // 2))