def numbersArray(numCount):
    array = []
    for _ in range(numCount):
        array.append(int(input('Число: ')))
    
    return array


def printArray(array):
    for n in array:
        print(n, end=' ')


def isSymmetrical(array):
    newArray = array.copy()
    if len(newArray) % 2 == 0:
        firsthalf, secondhalf = splitArray(newArray)
        if firsthalf == reversedArray(secondhalf):
            return True
    else:
        newArray.pop(len(newArray) // 2)
        firsthalf, secondhalf = splitArray(newArray)
        if firsthalf == reversedArray(secondhalf):
            return True
    
    return False


def reversedArray(array):
    newArray = []
    for n in range(len(array) - 1, -1, -1):
        newArray.append(array[n])
    
    return newArray


def splitArray(array):
    firsthalf, secondhalf = [], []
    for i in range(len(array)):
        if i + 1 <= len(array) // 2:
            firsthalf.append(array[i])
        else:
            secondhalf.append(array[i])
    
    return firsthalf, secondhalf


def completeArray(array):
    completion = array.copy()
    completion.pop(-1)
    if completion[-1] == array[-1]:
        completion.pop(-1)
    
    return reversedArray(completion), len(completion)


numCount = int(input('Кол-во чисел: '))
numbers = numbersArray(numCount)

print('\nПоследовательность:', end=' ')
printArray(numbers)
if isSymmetrical(numbers):
    print('\nПоследовательность симметрична, дописывать числа не требуется.')
else:
    reqNumbersArray, reqNumbersCount = completeArray(numbers)
    print('\nНужно приписать чисел:', reqNumbersCount)
    print('Сами числа:', end=" ")
    printArray(reqNumbersArray)
