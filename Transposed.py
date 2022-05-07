# print transposed of given list?

list_of_lists = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
transposed = [[row[i] for row in list_of_lists] for i in range(len(list_of_lists[0]))]
print(transposed)
