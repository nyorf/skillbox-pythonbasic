def shift_check(first_string, second_string):
    check_array = second_string[:]
    for shift in range(1, len(second_string)):
        check_array.append(check_array[0])
        check_array.pop(0)
        if check_array == first_string:
            return shift
    else:
        return 0
        

while True:
    first_string = list(input('Первая строка: '))
    second_string = list(input('Вторая строка: '))

    if len(first_string) != len(second_string):
        print('\nСтроки должны быть одинаковой длины!')
    elif first_string == second_string:
        print('\nСтроки должны быть разными!')
    else:
        break

result = shift_check(first_string, second_string)
if result != 0:
    print('\nПервая строка получается из второй со сдвигом {}.'.format(result))
else:
    print('\nПервую строку нельзя получить из второй с помощью циклического сдвига')
