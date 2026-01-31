# Krish's Approach

string = "count how many time the word word appeared in it"

find = "word"

string = string.split(" ")

count = 0

for _ in string:
    if find == _:
        count += 1

print(count)

# Dalip's Approach
sentence  = "eye for an eye"

word = "eye"
count = 0

for w in sentence.split(' '):
    if word in w:
        count+=1

print(f"Word repeating {count} times.")