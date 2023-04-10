employees = int(input('Введите количество сотрудников: '))
salaries = []
for employee in range(1, employees + 1):
      print('Зарплата', employee, 'сотрудника:', end=' ')
      salaries.append(int(input()))
while 0 in salaries:
    salaries.remove(0)

print('Осталось сотрудников:', len(salaries))
print('Зарплаты:', salaries)
print('\nМаксимальная зарплата:', max(salaries))
print('Минимальная зарплата:', min(salaries))
