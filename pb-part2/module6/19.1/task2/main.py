student_info = {}

info_request = input(
    'Введите информацию о студенте через пробел\n'
    '(имя, фамилия, город, место учёбы, оценки): '
).split()

student_info['Имя'] = info_request[0]
student_info['Фамилия'] = info_request[1]
student_info['Город'] = info_request[2]
student_info['Место учёбы'] = info_request[3]
student_info['Оценки'] = info_request[4:]

for key in student_info:
    print('{key} -- {value}'.format(key = key, value = student_info[key]))

print(len(student_info))
