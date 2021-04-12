def min_num(firstnumber, secondnumber):
    answer = ((firstnumber + secondnumber) - abs(firstnumber - secondnumber)) / 2
    print('Наибольшее число:', answer)

firstnumber = float(input('Введите первое число: '))
secondnumber = float(input('Введите второе число: '))
min_num(firstnumber, secondnumber)