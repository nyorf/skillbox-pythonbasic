def splitListToChunks(usrlist):
    chunkSize = len(usrlist) // 2
    splitList = [usrlist[i:i + chunkSize] for i in range(0, len(usrlist), chunkSize)]
    return splitList

def reversedCheck(usrlist):
    if list(reversed(usrlist[1])) == usrlist[0]:
        return True
    else:
        return False

def isSymmetrical(array):
    if len(array) % 2 != 0:
        array.pop(len(array) // 2)
        splitArray = splitListToChunks(array)
        return reversedCheck(splitArray)
    else:
        splitArray = splitListToChunks(array)
        return reversedCheck(splitArray)

def noRepeats(array):
    status = False
    for i_number in range(1, len(array)):
        if array[i_number - 1] < array[i_number]:
            status = True
    return status

def reverseListAndPrint(usrlist):
    usrlist = list(reversed(usrlist))
    print('Сами числа:', usrlist)


numbersCount = int(input('Введите количество чисел в последовательности: '))
sequence = []

for number in range(numbersCount):
    sequence.append(int(input('Число: ')))

originalSequence = sequence.copy()

print('\nПоследовательность:', end=' ')
for number in sequence:
    print(number, end='')

if isSymmetrical(sequence):
    print('\nДописывать числа не нужно, последовательность и так симметрична.')
else:
    checkSequence = sequence.copy()
    savedNumbers = []
    for i_num in range(len(checkSequence)):
        savedNumbers.append(checkSequence[i_num])
        checkSequence.pop(i_num)
        if isSymmetrical(checkSequence):
            break
    print("\nНужно приписать чисел:", len(savedNumbers))
    print('Сами числа:', savedNumbers)