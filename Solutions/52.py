def findMax(x):
    max = x[0]
    for i in range(0,len(x)):
        if(x[i]>max):
            max = x[i]
    return max

items = [2,5,8,4,3]

maximum= findMax(items)
print(f"The maximum number of The list is {maximum}")
    
