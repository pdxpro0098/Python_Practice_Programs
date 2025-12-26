# krish's Approach
str1 = "Write a Python program to find uncommon words from two strings"
str2 = "Write a Python Program to sort a dictionary by val two strings"

lst1 = sorted(str1.lower().split(" "))
lst2 = sorted(str2.lower().split(" "))

small = min(len(lst1), len(lst2))

for i in range(small):
    if lst1[i] != lst2[i]:
        print(lst1[i], lst2[i])

# Dalip's Approach
a = "save us from Titans"
b = "save us from Eren"

catalogue1 = a.upper().split()
catalogue2 = b.upper().split()

for i in range(0,len(catalogue1)):
    if catalogue1[i] != catalogue2[i]:
        print(catalogue1[i],catalogue2[i])
        
