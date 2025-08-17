lst = ["krish", 1, [], 5.6, "dilip", 0]
for item in lst:
    if not isinstance(item, int):
        lst.remove(item)

print(lst)