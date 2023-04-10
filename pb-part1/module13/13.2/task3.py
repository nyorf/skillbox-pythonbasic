def prioritymanager(queuecount):
    taskPriority = 0
    topPrioritysym = 0
    topTask = 0
    symcount = 0
    for tasks in range(queuecount):
        symcount = 0
        task = int(input('Введите число: '))
        if task < 0:
            taskPriority = 1
        else:
            for sym in str(task):
                symcount += 1
        if symcount > topPrioritysym:
            topTask = task
    return topTask

queue = int(input('Введите количество задач: '))
print('\nПервая задача на обработку:', prioritymanager(queue))
