line = list(range(160, 177, 2))
line_ext = line.extend(list(range(162, 181, 3)))

# или так, если всё закинуть в отдельную переменную
# line = []
# line.extend(class_one)
# line.extend(class_two)

line.sort()
print('Шеренга:', line)

# зачёт!
