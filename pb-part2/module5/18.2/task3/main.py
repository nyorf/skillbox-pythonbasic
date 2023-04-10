from ipaddress import ip_address


print('Введите IP-адрес четырьмя числами:\n')
ip_address = '{0}.{1}.{2}.{3}'
address_parts = [int(input('Введите число: ')) for _ in range(4)]
print(ip_address.format(
    address_parts[0], 
    address_parts[1],
    address_parts[2],
    address_parts[3]
    )
)

