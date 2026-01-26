# Krish's Appoach
lst = [12, 90, 14, [], 45, 6, [], 12, 14, [], [0], []]

for item in lst:
    if item == []:
        lst.remove(item)

print(lst)


# Dalip's Approach
def removeEmptyList(num):     
    for item in num:
        if len(item) == 0:
            num.remove(item)
    return num

num = [[2,5],[],[9,8]]
print(f"After removing empty one: {removeEmptyList(num)}")
