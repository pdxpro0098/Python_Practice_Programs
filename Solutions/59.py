# krish's Approach
lst = ["Write", "a", "Python", "program", "to", "find", "words",
       "which", "are", "greater", "than", "given", "length","k"]
k = 4
for word in lst:
    if len(word) > k:
        print(word)


# Dalip's Approach
def occurence(x,n):
    count = 0
    for i in x:
        if(x[i] == n):
            count += 1
    return count

items = [2,4,3,6,4,5,7,6,4]

number = int(input("Enter the number which you want to find: "))

occured = occurence(items,number)

print(f"Occurence of {number} is {occured}")
