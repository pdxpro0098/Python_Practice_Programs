str1 = "Write a Python program to find uncommon words from two strings"
str2 = "Write a Python Program to sort a dictionary by val two strings"

lst1 = sorted(str1.lower().split(" "))
lst2 = sorted(str2.lower().split(" "))

small = min(len(lst1), len(lst2))

for i in range(small):
    if lst1[i] != lst2[i]:
        print(lst1[i], lst2[i])
