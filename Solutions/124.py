s1 = "anagram"
s2 = "nagaram"

def isAnagram(string1,string2):
    if len(string1) != len(string2):
        return False
    for i in range(len(string1)):
        if string1[i] not in string2:
            return False
    return True

print(isAnagram(s1,s2))