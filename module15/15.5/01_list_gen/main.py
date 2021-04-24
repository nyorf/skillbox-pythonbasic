def isOdd(number):
    if number % 2 != 0:
        return True
    else:
        return False


numlist = []
endnum = int(input('Введите конечное число: '))

for num in range(1, endnum + 1):
    if isOdd(num):
        numlist.append(num)

print(numlist)