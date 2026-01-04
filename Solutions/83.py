
string = "count how many time the word word appeared in it"

find = "word"

string = string.split(" ")

count = 0

for _ in string:
    if find == _:
        count += 1

print(count)
