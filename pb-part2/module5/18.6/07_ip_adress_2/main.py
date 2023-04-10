def check_ip(ip):
    if len(ip) != 4:
        print('IP-адрес -- это четыре числа, разделённые точками.', end='\n\n')
        return False

    for num in ip:
        if not num.isdigit():
            print('{} -- не целое число. Попробуйте снова.'.format(num), end='\n\n')
            return False
        elif num.isdigit() and int(num) > 255:
            print('{} превышает {}. Попробуйте снова.'.format(num, 255), end='\n\n')
            return False

    return True


while True:
    ip = input('Введите IP-адрес: ').split('.')

    if check_ip(ip):
        print('IP-адрес {} корректен.'.format('.'.join(ip)), end='\n\n')
        break

# зачёт!
