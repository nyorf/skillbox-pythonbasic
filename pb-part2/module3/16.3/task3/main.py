packet = []
decoded_message = []
totalErrors = 0
bad_packets = 0

packets_count = int(input('Введите количество пакетов: '))

for i_packet in range(1, packets_count + 1):
    print('\nПакет №' + str(i_packet))
    for i_bit in range(1, 5):
        print(str(i_bit), 'бит:', end=' ')
        packet.append(int(input()))
    if packet.count(-1) > 1:
        bad_packets += 1
        print('Много ошибок в пакете.')
    else:
        totalErrors += packet.count(-1)
        decoded_message.extend(packet)
    packet = []

print('\nПолученное сообщение:', decoded_message)
print('Количество ошибок в сообщении:', totalErrors)
print('Количество потерянных пакетов:', bad_packets)