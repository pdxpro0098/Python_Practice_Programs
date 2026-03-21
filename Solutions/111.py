# Krish's Approach
lst = ["krish", 1, [], 5.6, "dilip", 0]
for item in lst:
    if not isinstance(item, int):
        lst.remove(item)

print(lst)

# Dalip's Approach
userName = ["d", "a", "l", "i", "p", "2", "3", "4"]

newlist = list(filter(str.isdigit, userName))
print(newlist)
