apt_price = int(input('Введите стоимость квартиры: '))
apt_size = int(input('Введите площадь квартиры (кв.м): '))
if apt_size < 0 or apt_price < 0:
    exit('Оба числа должны быть больше нуля!')
else:
    if (apt_size >= 100 and apt_price <= 10000000) or ((apt_size >= 80 and apt_size <= 99) and apt_price <= 7000000):
        print('Эта квартира нам подходит!')
    else:
        print('Эта квартира нам не подходит. Ищем дальше!')