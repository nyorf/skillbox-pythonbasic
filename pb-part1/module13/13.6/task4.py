def expnum(number):
    isMantisse = True
    isOrder = False
    mantisse = ''
    order = ''
    for sym in number:
        if sym == 'e' or sym == 'E':
            isMantisse = False
            isOrder = True
        elif isMantisse:
            mantisse += sym
        elif isOrder:
            order += sym
    return mantisse, order

mantisse, order = expnum(input('Введите число в эксп. форме: '))
print('Мантисса =', str(mantisse) + ';', 'порядок =', order)