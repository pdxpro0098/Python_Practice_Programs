# Krish's Approach
lst = [12,34,56,78,999]
print(max(lst))

# Dalip's Approach
def findMin(x):
    min = x[0]
    for i in range(0,len(x)):
        if(x[i]<min):
            min = x[i]
    return min

items = [9,5,6,4,3]

minimum = findMin(items)
print(f"The minimum number of The list is {minimum}")
