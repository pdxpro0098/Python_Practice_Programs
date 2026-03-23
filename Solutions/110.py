# Krish's Approach
word = "FindCapitalLetters"
indexes = []
for i in range(len(word)):
    if ord(word[i]) < 97:
        indexes.append(i)

print(indexes)

# Dalip's Approach
name = "DalipKumar"
i = 0
for i in range(len(name)):
    if name[i] == name[i].upper():
        print(f"Character: {name[i]} Index: {i}")

