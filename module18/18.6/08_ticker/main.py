def shift_check(first_string, second_string):
    # TODO, предлагаю производить сдвиг без использования вложенного цикла.
    #  При помощи срезов, в одну строку кода.
    check_array = second_string[:]
    for shift in range(1, len(second_string)):
        check_array[:shift], check_array[-shift:] = check_array[-shift:], check_array[:shift]

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
