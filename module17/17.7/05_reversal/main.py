string = input('Введите строку: ')

h_indexes = [string.index('h')]

for i in range(-1, -len(string) - 1, -1):
    if string[i] == 'h':
        h_indexes.append(i)
        break

print('Развернутая последовательность между первым и последним h:', string[h_indexes[1] - 1:h_indexes[0]:-1])
