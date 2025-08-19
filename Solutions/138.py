with open("temp.txt", "r") as f:
    temp = f.read()

with open("temp2.txt", "r") as f:
    temp2 = f.read()

with open("main.txt", "w") as f:
    f.write(temp)
    f.write("\n")
    f.write(temp2)