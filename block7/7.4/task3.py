wakeuptime = int(input('Во сколько проснулся? '))
calories_total = 0
awake_hours = 0
for hour in range(wakeuptime, 23):
    print('Текущий час:', hour)
    hourly_calories = int(input('Сколько калорий получено за этот час? '))
    calories_total += hourly_calories
    if calories_total > 2000:
        print('Хорошо поел, теперь можно и поспать!')
        print('Всего съедено калорий:', calories_total)
        break
    awake_hours += 1
print('Саша не спал', awake_hours, 'часов')