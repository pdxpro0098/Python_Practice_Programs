string = "Write a Python Program to count the number of each character in a string"
wordMap = dict()

for char in string:
    if char in wordMap:
        wordMap[char] += 1
    else:
        wordMap[char] = 1

print(wordMap)
