initial_list = [1, 2, 3, 4, 5]
updated_list = []
movefor = int(input('Сдвиг: '))

counter = 0
while counter != -movefor:
    counter -= 1
    updated_list.append(initial_list[counter])

for entry in range(len(initial_list) - movefor):
    updated_list.append(initial_list[entry])

print('Изначальный список:', initial_list)
print('Сдвинутый список:', updated_list)