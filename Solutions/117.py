string = "Hello World"


def reverse_string(s):
    revStr = ""
    for i in range(len(s)):
        revStr += s[len(s)-i-1]
    return revStr


print(reverse_string(string))