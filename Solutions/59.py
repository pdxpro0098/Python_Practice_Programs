# Krish's Approach
lst = [
    "Write",
    "a",
    "Python",
    "program",
    "to",
    "find",
    "words",
    "which",
    "are",
    "greater",
    "than",
    "given",
    "length",
    "k",
]
k = 4
for word in lst:
    if len(word) > k:
        print(word)

# Dalip's Approach
words = [
    "misogynist",
    "narcissist",
    "claustrophobic",
    "lad",
    "pensive",
    "cuisine",
    "paradox",
]

k = int(input("Enter the length: "))


extractedWords = [word for word in words if len(word) >= k]

print(extractedWords)
