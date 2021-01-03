# Задача 7. Обычный день на работе
# Максим программирует целый день на работе и вечером идет домой. Каждый час начальство кидает ему несколько задач,
# которые ему нужно решить до следующего рабочего часа. И вдобавок каждый час Максиму звонит супруга.
# Он знает, что если он возьмёт трубку, то жена попросит зайти вечером в магазин.
# Напишите программу, в которой считается сколько задач выполнил Максим за день (8 часов)
# и если он хоть раз взял трубку, то в конце дополнительно вывести сообщение “Нужно зайти в магазин”.
print('Начался 8-часовой рабочий день.')
hourcounter = 0
taskcounter = 0
callcounter = 0
while hourcounter < 8:
    hourcounter += 1
    print(hourcounter, 'час')
    taskcounter += int(input('Сколько задач решит Максим? '))
    callcounter += int(input('Звонит жена. Взять трубку? (1 - да, 0 - нет) '))
print('Рабочий день закончился. Всего выполнено задач:', taskcounter)
if callcounter > 0:
    print('Нужно зайти в магазин!')