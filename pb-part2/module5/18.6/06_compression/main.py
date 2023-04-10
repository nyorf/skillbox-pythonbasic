import re
from itertools import groupby

def solution_regex(string):
    groups = [char.group(0) for char in re.finditer(r"(\w)\1*", string)]
    encoded_string = ''.join(['{}{}'.format(groups[i][0], len(groups[i])) 
                                for i in range(len(groups))])
    
    return encoded_string

def solution_itertools(string):
    groups = ["".join(group) for _, group in groupby(string)]
    encoded_string = ''.join(['{}{}'.format(groups[i][0], len(groups[i])) 
                                for i in range(len(groups))])
    
    return encoded_string

string = input('Введите строку: ')

print('Закодированная строка:', solution_itertools(string))

# TODO, пожалуйста, обратите внимание, модули re и itertools в текущем уроке лишние.
#  До них мы дойдём в 30 модуле. Стоит решить задание методами из пройденных уроков.