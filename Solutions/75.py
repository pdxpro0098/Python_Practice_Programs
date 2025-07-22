string = "Write,a,Python,Program,to,sort,a,comma,separated,sequence,of,words,alphabetically"

s = sorted(string.replace(",",""))

for c in s:
    print(c,end=" ")