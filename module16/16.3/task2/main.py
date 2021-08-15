def symbolcounter(msg):
    return msg.count('?') + msg.count('!')

first_msg = input('Первое сообщение: ')
second_msg = input('Второе сообщение: ')

if symbolcounter(first_msg) > symbolcounter(second_msg):
    print('Третье сообщение:', first_msg, second_msg)
elif symbolcounter(first_msg) < symbolcounter(second_msg):
    print('Третье сообщение:', second_msg, first_msg)
else:
    print('Ой')
