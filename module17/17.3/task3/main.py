from random import randint

first_squad_dmg = [randint(50, 80) for _ in range(10)]
second_squad_dmg = [randint(30, 60) for _ in range(10)]
third_squad_status = ['Погиб' if first_squad_dmg[player] + second_squad_dmg[player] > 100 
                        else 'Выжил' for player in range(10)]

print('Урон первого отряда:', first_squad_dmg)
print('Урон второго отряда:', second_squad_dmg)
print('Состояние третьего отряда:', third_squad_status)
