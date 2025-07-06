string = "01010101010"
flag = True
for char in range(len(string)-1):
    if string[char] == string[char+1]:
        flag = False
        break

print("Binary string" if flag else "not binary string")
