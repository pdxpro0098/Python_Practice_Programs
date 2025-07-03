lst = ["Write", "a", "Python", "program", "to", "find", "words",
       "which", "are", "greater", "than", "given", "length","k"]
k = 4
for word in lst:
    if len(word) > k:
        print(word)
