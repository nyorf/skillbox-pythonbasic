totalSoldiers = int(input('Сколько всего солдат? '))
totalRules = 0
totalPushups = 0
for soldier in range(totalSoldiers - 4, 0, -4):
    print('Солдат под номером', soldier)
    totalRules = int(input('Сколько правил спросить у солдата? '))
    soldierAnswer = int(input('Эй, солдат, сколько правил в этом уставе? '))
    if soldierAnswer != totalRules:
        pushups = soldier * 10
        print('Неправильно, солдат!', pushups, 'отжиманий!')
        totalPushups += pushups
    else:
        print('Молодец, солдат!')
print('Всего солдаты отжались', totalPushups, 'раз.')