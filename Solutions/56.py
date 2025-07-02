lst = [12, 90, 14, [], 45, 6, [], 12, 14, [], [0], []]

for item in lst:
    if item == []:
        lst.remove(item)

print(lst)
