encryptedMessage = input('Введите зашифрованное сообщение: ')
currentLetter = 0
decryptedPartOne = ''
decryptedPartTwo = ''
for letter in encryptedMessage:
    currentLetter += 1
    if (currentLetter + 1) % 2 == 0:
        decryptedPartOne += letter
    elif currentLetter % 2 == 0:
        decryptedPartTwo = letter + decryptedPartTwo
decryptedMessage = decryptedPartOne + decryptedPartTwo
print('Расшифрованное сообщение:', decryptedMessage)
