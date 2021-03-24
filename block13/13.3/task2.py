def inputcontrol():
    number = input('\nВведите число в эксп. форме: ')
    mantisse = ''
    if 0 < float(number) < 1:
        for sym in number:
            if sym != 'e' or sym != 'E':
                mantisse = mantisse + sym
            else:
                break
            if 1 <= float(mantisse) <= 9:
                return(float(number))
            else:
                print('Пожалуйста, введите число в эксп. форме с мантиссой от 1 до 9! [(1-9)e-(1-...)]')
                inputcontrol()
    else:
        print('Пожалуйста, проверьте введённое вами число. [(1-9)e-(1-...)]')
        inputcontrol()

reqNumber = 1
counter = 0
expnumber = inputcontrol()
while reqNumber < 2:
    counter += 1
    reqNumber += expnumber
print('Количество прибавлений:', counter)