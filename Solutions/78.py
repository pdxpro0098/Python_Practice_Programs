# Krish's Approach
char = 0
digit = 0

for c in string:
    if c.isalpha():
        char += 1
    elif c.isdigit():
        digit += 1

print(char)
print(digit)


# Dalip's Approach
def fetchNoOfDigitsOrLetters(s,d,l):
    for ch in s:
        if ord(ch) >=65 and ord(ch) <= 90: # A-Z
            l+=1
        elif ord(ch) >=48 and ord(ch) <= 57: # 0-9
            d+=1 
    return l,d

sentence = list("hello world34".upper())

letters,digits = fetchNoOfDigitsOrLetters(sentence,0,0)

print(f"Letters: {letters} digits: {digits}")