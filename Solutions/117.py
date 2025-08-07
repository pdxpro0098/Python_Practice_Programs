def stringReverse(name_list,length):
    start = 0
    end = length - 1
    while start <= end:
        name_list[start],name_list[end] = name_list[end],name_list[start]   
        start += 1
        end -= 1
    return ' '.join(name_list)


name = "ENOLA"
name_list = list(name)
length = len(name)


print(stringReverse(name_list,length))  
