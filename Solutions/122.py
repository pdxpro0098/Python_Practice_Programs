# Dalip's Approach
def reverseString(name_list, length):
    name_list = list(name)  
    start = 0
    end = length - 1
    while start <= end:
        name_list[start], name_list[end] = name_list[end], name_list[start]
        start += 1
        end -= 1
    return ' '.join(name_list)
  
name = "ENOLA"
length = len(name)

print(reverseString(name, length))



