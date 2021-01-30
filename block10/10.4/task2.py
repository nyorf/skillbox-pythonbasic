totalNumbers = int(input('Сколько чисел дано? '))
reqNum = 5
answer = 0
for num in range(1, totalNumbers + 1):
    print('Введите', str(num), end='')
    number = int(input('-e число: '))
    while number != 0:
        lastDigit = number % 10
        if lastDigit > 5:
            answer += 1
        number //= 10
print('Количество цифр больше', str(reqNum) + ':', answer)