string = input('Введите строку: ')

print('Развернутая последовательность между первым и последним h:',
      string[string.rindex('h') - 1:string.index('h'):-1])

# зачёт!
