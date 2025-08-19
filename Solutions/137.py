temp = ""
with open("temp.txt", "r") as f:
    for line in f:
        temp += f.read()

with open("temp2.txt", "w") as f:
    f.write(str(temp))