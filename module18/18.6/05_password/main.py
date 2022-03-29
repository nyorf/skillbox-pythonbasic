while True:
    password = input('Придумайте пароль: ')

    params_length = len(password)
    params_upper = 0
    params_decimals = 0

    for sym in password:
        if sym.isupper():
            params_upper += 1
        elif sym.isdecimal():
            params_decimals += 1

    if params_length < 8:
        print('Пароль ненадёжный. Он должен состоять как минимум из 8 символов.', end='\n\n')
    elif params_upper < 1:
        print('Пароль ненадёжный. В нём должна быть минимум одна заглавная буква.', end='\n\n')
    elif params_decimals < 3:
        print('Пароль ненадёжный. В нём должно быть минимум 3 цифры.', end='\n\n')
    else:
        print('Это надёжный пароль!', end='\n\n')
        break
