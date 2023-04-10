message = input('Введите строку: ')
add_symbol = input('Введите дополнительный символ: ')

doubled_symbols = [sym * 2 for sym in message]
doubled_with_addsymbol = [d_sym + add_symbol for d_sym in doubled_symbols]

print('\nСписок удвоенных символов:', doubled_symbols)
print('Склейка с дополнительными символами:', doubled_with_addsymbol)
