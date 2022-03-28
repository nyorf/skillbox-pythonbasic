#from string import punctuation

def reverse(text):
    array = list(text)
    array.reverse()
    return ''.join(array)

def remove_pm(text):
    removed_symbols = []

    for sym in text:
        if not sym.isalnum():
            removed_symbols.append([sym, text.find(sym)])
            text = text.replace(sym, '@', 1)
    
    return text, removed_symbols

def reverse_message(text):
    text = text.split('@')
    reversed_msg = [reverse(word) for word in text]
    return reversed_msg

def replace_pm(array, removed_symbols):
    text = ''.join(array)
    for i in range(len(removed_symbols)):
        text = text[:removed_symbols[i][1]] + removed_symbols[i][0] + text[removed_symbols[i][1]:]
    
    return text

def action(msg):
    edited_msg, removed_symbols = remove_pm(msg)
    edited_msg = reverse_message(edited_msg)
    edited_msg = replace_pm(edited_msg, removed_symbols)
    return edited_msg


message = input('Введите сообщение: ')
print('Новое сообщение: {}'.format(action(message)))


