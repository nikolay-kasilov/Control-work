"""
Сделайте функцию, которая создаст новый список из этого, заменив None на 0
"""

test_lst = [
    [1, 2, 3],
    [4, 5, 6],
    [None, 8, 9],
    [10, 11, 12],
    [13, None, 15],
    [16, 17, 18],
    [19, 20, 21],
    [22, 23, None],
]
for i in range(len(test_lst)):
    for j in range(len(test_lst[i])):
        if test_lst[i][j] == None:
            test_lst[i][j] = 0



print (test_lst)