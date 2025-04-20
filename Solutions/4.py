def swap(a,b):
    print(f"The previous value \n a = {a} \n b = {b}")
    temp = a
    a = b 
    b = temp
    result = f"The swapped value \n a = {a} \n b = {b}"
    print(result)
    return result

swap(34,65)
