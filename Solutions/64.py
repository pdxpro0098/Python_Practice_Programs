string = "64. Write a Python Program to find duplicate characters in a string."

dupChar: list[str] = []

string = string.replace(" ", "")
string = sorted(string)

for i in range(len(string)-1):
    if string[i] == string[i+1]:
        if string[i] not in dupChar:
            dupChar.append(string[i])

print(dupChar)
