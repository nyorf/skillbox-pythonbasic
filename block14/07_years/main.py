startyear = int(input('Введите первый год: '))
endyear = int(input('Введите второй год: '))

print('\nГода от', startyear, 'до', endyear, 'с тремя одинаковыми цифрами:')
for year in range(startyear, endyear + 1):
    firstdigit = 0
    firstdigitcounter = 0
    seconddigit = 0
    seconddigitcounter = 0
    counter = 0
    for digit in str(year):
        counter += 1
        if counter == 1:
            firstdigit = int(digit)
            firstdigitcounter += 1
        elif counter == 2:
            seconddigit = int(digit)
            seconddigitcounter += 1
        else:
            if int(digit) == firstdigit:
                firstdigitcounter += 1
            elif int(digit) == seconddigit:
                seconddigitcounter += 1
    if firstdigitcounter == 3 or seconddigitcounter == 3:
        print(year)