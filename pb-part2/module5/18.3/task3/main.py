template = input('Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}')
while True:
    names = input('Введите имена (через запятую): ').split(', ')
    ages = input('Введите возраста (через запятую): ').split(', ')
    if len(names) == len(ages):
        break
    else:
        print('\nКоличество имён не совпадает с количеством возрастов.')
        print('Попробуете снова?\n')

for i in range(len(names)):
    print(template.format(
        name=names[i],
        age=ages[i]
    )
)

people = [' '.join([names[i], ages[i]]) for i in range(len(names))]

print('\nИменинники:', end=' ')
output = ', '.join(people)
print(output)
