word = "FindCapitalLetters"
indexes = []
for i in range(len(word)):
    if ord(word[i]) < 97:
        indexes.append(i)

print(indexes)