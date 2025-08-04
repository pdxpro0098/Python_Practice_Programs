lst = [(122, 34), (12, 21), (90, 87), (33, 45)]
sorted_list = sorted(dict(lst).items(), key=lambda item: item[1])
print(sorted_list)
