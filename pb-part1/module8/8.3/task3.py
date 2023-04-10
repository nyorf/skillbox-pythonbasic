wakeuptime = int(input('Во сколько проснулся? '))
water = 0
calories = 0
for hour in range(wakeuptime, 23, 3):
    print('Час:', hour)
    water += 1
    calories += int(input('Сколько калорий съел? '))
print('Литров воды выпито:', water)
print('Калорий съедено:', calories)