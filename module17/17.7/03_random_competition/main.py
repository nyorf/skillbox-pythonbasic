from random import uniform

first_team = [round(uniform(5, 10), 2) for _ in range(20)]
second_team = [round(uniform(5, 10), 2) for _ in range(20)]
winners = [first_team[player] if first_team[player] > second_team[player]
            else second_team[player] for player in range(20)]

print('Первая команда:', first_team)
print('Вторая команда:', second_team)
print('Победители тура:', winners)
