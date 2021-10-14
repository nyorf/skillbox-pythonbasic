def splitListToChunks(usrlist):
    chunkSize = len(usrlist) // 2
    splitList = [usrlist[i:i + chunkSize] for i in range(0, len(usrlist), chunkSize)]
    return splitList


def reversedCheck(usrlist):
    if list(reversed(usrlist[1])) == usrlist[0]:
        return True
    else:
        return False


def isSymmetrical(sequence):
    if len(sequence) % 2 != 0:
        sequence.pop(len(sequence) // 2)
        splitSequence = splitListToChunks(sequence)
        return reversedCheck(splitSequence)
    else:
        splitSequence = splitListToChunks(sequence)
        return reversedCheck(splitSequence)


def reverseListAndPrint(usrlist):
    usrlist = list(reversed(usrlist))
    print('Сами числа:', usrlist)


numbersCount = int(input('Введите количество чисел в последовательности: '))
sequence = []

for number in range(numbersCount):
    sequence.append(int(input('Число: ')))

print('\nПоследовательность:', end=' ')
for number in sequence:
    print(number, end='')

if isSymmetrical(sequence):
    print('\nДописывать числа не нужно, последовательность и так симметрична.')
elif sequence[-1] == sequence[-2]:
    print('\nНужно приписать чисел:', len(sequence) - 2)
    requiredNumbers = sequence.copy()
    for _ in range(2):
        requiredNumbers.pop(-1)
    reverseListAndPrint(requiredNumbers)
else:
    print('\nНужно приписать чисел:', len(sequence))
    requiredNumbers = sequence.copy()
    reverseListAndPrint(requiredNumbers)


# Введите количество чисел в последовательности: 5
# Число: 1
# Число: 2
# Число: 1
# Число: 2
# Число: 1
#
# Последовательность: 12121
# Нужно приписать чисел: 5
# Сами числа: [1, 2, 1, 2, 1]
# TODO, если список симметричен, добавлять в него новые числа не нужно
#  Предлагаю попробовать идти в цикле по списку чисел и проверять, является ли список палиндромным или нет.
#  [1, 2, 1, 2, 1, 2] - если нет, сохраняем первое число (1) и проверяем от второго числа и до конца списка.
#  [2, 1, 2, 1, 2] - если да, значит в конец списка [1, 2, 1, 2, 1, 2] стоит добавить 1, чтобы список стал палиндромным.
