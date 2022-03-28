while True:
    password = input('Придумайте пароль: ')
    parameters = [len(password), 0, 0]

    for sym in password:
        if sym.isupper():
            parameters[1] += 1
        elif sym.isdecimal():
            parameters[2] += 1

    if parameters[0] < 8:
        print('Пароль ненадёжный. Он должен состоять как минимум из 8 символов.', end='\n\n')
    elif parameters[1] < 1:
        print('Пароль ненадёжный. В нём должна быть минимум одна заглавная буква.', end='\n\n')
    elif parameters[2] < 3:
        print('Пароль ненадёжный. В нём должно быть минимум 3 цифры.', end='\n\n')
    else:
        print('Это надёжный пароль!', end='\n\n')
        break
