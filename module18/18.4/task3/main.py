string = input('Введите строку: ')
cases = [0 for _ in range(2)]

for letter in string:
    if letter.islower():
        cases[0] += 1
    elif letter.isupper():
        cases[1] += 1

if cases[0] > cases[1]:
    string = string.lower()
elif cases[1] > cases[0]:
    string = string.upper()

print('Результат:', string)
