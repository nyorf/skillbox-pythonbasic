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
        # TODO Предлагаю попробовать сократить количество повторяющихся строк кода до одной.
        #  Если строка встречается в каждом блоке условного оператора, стоит подумать, как вынести её за пределы условного оператора.
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
    completion, newArray = [], array.copy()
    while len(newArray) > 1:
        completion.append(newArray[0])
        newArray.pop(0)
        if isSymmetrical(newArray):
            return reversedArray(completion), len(completion)
    
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
