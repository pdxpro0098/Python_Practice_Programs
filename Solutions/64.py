# Krish's Approach
string = "a a b c c d "

dupChar: list[str] = []

string = string.replace(" ", "")
string = sorted(string)

for i in range(len(string)-1):
    if string[i] == string[i+1]:
        if string[i] not in dupChar:
            dupChar.append(string[i])

print(dupChar)


# Dalip's Approach
def findDuplicatesFromString(persons):
    duplicates = []
    for i in range(len(persons)):
        for j in range(i+1,len(persons)):
            if(persons[i]==persons[j]):
                duplicates.append(persons[j])
    return ",".join(duplicates);

persons = "adam & eve"

print(f"Duplicates from string seperated by ',':  {findDuplicatesFromString(persons)}")
