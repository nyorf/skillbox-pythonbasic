def dataRequest(surname, name, country, city, street, streetnum, aptnum):
    print('\nФамилия:', name)
    print('Имя:', surname)
    print('Страна проживания:', country)
    print('Город:', city)
    print('Улица:', street)
    print('Номер дома:', streetnum)
    print('Номер квартиры:', aptnum)

surname = input('Введите фамилию: ')
name = input('Введите имя: ')
country = input('Введите страну проживания: ')
city = input('Введите город: ')
street = input('Введите улицу: ')
streetnum = input('Введите номер дома: ')
aptnum = int(input('Введите номер квартиры: '))

dataRequest(surname, name, country, city, street, streetnum, aptnum)