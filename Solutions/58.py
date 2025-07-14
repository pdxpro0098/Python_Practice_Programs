lst = [1, 1, 1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7, 8, 9, 9, 10, 10, 10, 10, 10]

lstMap = dict()

for val in lst:
    if val not in lstMap:
        lstMap[val] = 1
    else:
        lstMap[val] += 1

print(lstMap)
