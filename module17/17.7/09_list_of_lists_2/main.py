nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new_list = [elem for i in range(len(nice_list)) 
            for j in range(len(nice_list[i])) 
            for elem in nice_list[i][j]]

print(new_list)

# придумал только как решить проблему с "если добавить ещё элемент то сломается"
# пока не знаю как можно сделать по другому, без range
