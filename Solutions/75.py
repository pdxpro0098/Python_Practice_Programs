# Krish's Approach
string = "Write,a,Python,Program,to,sort,a,comma,separated,sequence,of,words,alphabetically"

s = sorted(string.replace(",",""))

for c in s:
    print(c,end=" ")


# Dalip's Approach
def sortInAlphabeticalOrder(b):
    n=len(b)
    for i in range(n):
        for j in range(n-1):
            if b[j]>b[j+1]:
                b[j],b[j+1] = b[j+1],b[j]
    return ",".join(b)
a = "dalip,arti,isha,priya,43"
b = a.split(",")
print(sortInAlphabeticalOrder(b))