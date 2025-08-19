with open("temp.txt", "r") as file:
    allWords = file.read()
    
allWords = allWords.replace(".", "").replace("#", "")


def countWord(string):
    words = string.split()
    return len(words)


print(countWord(allWords))
