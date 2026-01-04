# Krish's Approach
lst = [12,34,56,78,999]
print(max(lst))

# Dalip's Approach
def findMax(x):
    max = x[0]
    for i in range(0,len(x)):
        if(x[i]>max):
            max = x[i]
    return max

items = [9,5,6,4,3]

maximum = findMax(items)
print(f"The maximum number of The list is {maximum}")
