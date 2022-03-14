string = input('Введите строку: ')

h_indexes = [string.index('h')]

for i in range(-1, -len(string) - 1, -1):
    if string[i] == 'h':
        h_indexes.append(i)
        break

print('Развернутая последовательность между первым и последним h:', string[h_indexes[1] - 1:h_indexes[0]:-1])

# TODO, пожалуйста, обратите внимание, циклы в данном задании не нужны,
#  предлагаю попробовать решить только при помощи поиска элементов по индексу и срезам.
#  Ознакомиться с методами index и rindex, и их параметрами можно:
#  https://pythonz.net/references/named/str.rindex/
#  https://pythonz.net/references/named/str.index/

