# krish's Approach
string = "01010101010"
flag = True
for char in range(len(string)-1):
    if string[char] == string[char+1]:
        flag = False
        break

print("Binary string" if flag else "not binary string")

# Dalip's Approach
binaryString = input("Enter binary no: ")

for i in binaryString:
    if i not in ('1','0'):
        print("It's not an binary string!")
        break
else:
    print("It's an binary string.")

