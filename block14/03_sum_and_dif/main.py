def alldigitsumm(number):
    result = 0
    for digit in str(number):
        result += int(digit)
    return result

def digitcounter(number):
    result = 0
    for digit in str(number):
        result += 1
    return result


number = int(input('Введите число: '))
digitsumm, digitcount = alldigitsumm(number), digitcounter(number)

print('\nСумма цифр:', digitsumm)
print('Количество цифр в числе:', digitcount)
print('Разность суммы и количества цифр:', digitsumm - digitcount)