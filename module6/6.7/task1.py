# Задача 1. Кубы чисел
# Любителю математики Паше снова стало мало распечатанных табличек, включая последнюю со степенями двойки.
# Теперь он хочет взять третью степень чисел от 1 до абсолютно любого!
# Напишите программу, которая возводит в третью степень каждое число от 1 до N и выводит на экран.
num = 0
end_num = int(input('До какого числа нужно возводить всё в 3 степень? '))
num_power = 3
output_num = 0
while num != end_num:
    num += 1
    output_num = num ** num_power
    print(output_num)