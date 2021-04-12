bags_total = int(input('Сколько всего мешков? '))
weight_total = 0
bags_counter = 0
while bags_counter < bags_total:
    bag_weight = int(input('Сколько весит этот мешок? '))
    weight_total += bag_weight
    bags_counter += 1
print('Всего мешки весят', weight_total, 'кг')
