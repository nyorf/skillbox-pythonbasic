workers = []
workers_count = int(input('Введите количество сотрудников в офисе: \n'))

for _ in range(workers_count):
    worker_id = int(input('Введите ID сотрудника: '))
    workers.append(worker_id)

worker_search = int(input('\nКакой ID ищем? '))
isFound = False
for worker in workers:
    if worker == worker_search:
        isFound = True

if isFound:
    print('\nСотрудник под номером', worker_search, 'работает')
else:
    print('\nСотрудник под номером', worker_search, 'не работает!')