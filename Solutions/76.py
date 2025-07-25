# ✅ 76. Write a Python Program to remove duplicate words and sort them alphanumerically.
s = "remove duplicate duplicate words from from this string string"
noDuplicate = set(s.split(" "))


print(sorted(noDuplicate))