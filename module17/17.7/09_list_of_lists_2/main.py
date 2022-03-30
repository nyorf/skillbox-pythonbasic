nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new_list = [elem for second_layer in nice_list for first_layer in second_layer for elem in first_layer]

print(new_list)
