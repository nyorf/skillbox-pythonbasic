def expnum(number):
    counter = 0
    mantissecounter = 0
    mantisse = ''
    order = ''
    for sym in number:
        if sym == 'e' or sym == 'E':
            break
        mantissecounter += 1
        mantisse += sym
    for sym in number:
        if counter > mantissecounter:
            order += sym
        else:
            counter += 1
    return mantisse, order

mantisse, order = expnum(input('Введите число в эксп. форме: '))
print('Мантисса =', str(mantisse) + ';', 'порядок =', order)