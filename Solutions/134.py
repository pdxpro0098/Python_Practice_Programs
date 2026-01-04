# Krish's Approach
with open("temp.txt", "r") as file:
    allWords = file.read()
    
allWords = allWords.replace(".", "").replace("#", "")


def countWord(string):
    words = string.split()
    return len(words)


print(countWord(allWords))

# Dalip's Approach
def  cout_word_in_file(fileName):
    try:
        with open(fileName,"r") as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print("File not found!")
        return 0
    
fileName = 'dalip.txt'
word_count = cout_word_in_file(fileName)
print(f"Total words in '{fileName}': {word_count} ")
