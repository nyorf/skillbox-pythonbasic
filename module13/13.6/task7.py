def numrequest():
    while True:
        startamp = float(input('Введите начальную амплитуду: '))
        stopamp = float(input('Введите амплитуду остановки: '))
        if startamp < stopamp or startamp == stopamp:
            print('Проверьте правильность введённых данных!')
        else:
            return startamp, stopamp

def count():
    startamp, stopamp = numrequest()
    currentamp = startamp
    counter = 0
    while currentamp > stopamp:
        currentamp = currentamp - (currentamp * 0.084)
        counter += 1
    return counter


print('Маятник считается остановившимся через', count(), 'колебаний')