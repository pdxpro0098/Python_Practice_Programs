# krish's Approach
string = "split this string"
lst = string.split(" ")
print(lst)

strLst = ["join", "this", "string"]
string = " ".join(strLst)
print(string)

# Dalip's Approach
text = "I Love Philadelphia"

word = text.split() # Word becomes a list
print(word) 

word.remove("Love")
sentence = ' '.join(word)

print(sentence)
