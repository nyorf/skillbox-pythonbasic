'''
string = input('Введите строку: ').split()
capitalized_string = ' '.join([word.capitalize() for word in string])

print('Результат:', capitalized_string)
'''
string = input('Введите строку: ').title()
print('Результат:', string)
