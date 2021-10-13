def isSymmetrical(sequence):
    if len(sequence) % 2 != 0:
        return False
    else:
        chunkSize = len(sequence) // 2
        splitSequence = [sequence[i:i + chunkSize] for i in range(0, len(sequence), chunkSize)]
        if list(reversed(splitSequence[1])) == splitSequence[0]:
            return True
        else:
            return False

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
    requiredNumbers = list(reversed(requiredNumbers))
    print('Сами числа:', requiredNumbers)
else:
    print('\nНужно приписать чисел:', len(sequence))
    requiredNumbers = sequence.copy()
    requiredNumbers = list(reversed(requiredNumbers))
    print('Сами числа:', requiredNumbers)