lst = [1,2,3,4,5,6]
split_index = len(lst) // 2
res = lst[split_index:] + lst[:split_index]
print(res)