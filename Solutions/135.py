lst = list()
with open("temp.txt", "r") as f:
    line = f.readlines()
    lst.append(line)

print(lst)