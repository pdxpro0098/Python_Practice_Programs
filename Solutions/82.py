# Krish's Approach
lst = [(122, 34), (12, 21), (90, 87), (33, 45)]
sorted_list = sorted(dict(lst).items(), key=lambda item: item[1])
print(sorted_list)


# Dalip's Approach
def sortOnTwoElements(items):
    for i in range(len(items)):
        a,b = items[i]
        if(a>b):
            items[i] = (b,a)
    return items

tuple_items=[(1,4),(3,2),(5,4),(9,8)]

print("Sorted Tuple:")        
print(sortOnTwoElements(tuple_items))
