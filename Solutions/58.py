# Krish's Approach
lst = [1, 1, 1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7, 8, 9, 9, 10, 10, 10, 10, 10]

lstMap = dict()

for val in lst:
    if val not in lstMap:
        lstMap[val] = 1
    else:
        lstMap[val] += 1

print(lstMap)

# Dalip's Approach
def occurence(x,n):
    count = 0
    for i in x:
        if(x[i] == n):
            count += 1
    return count

items = [2,4,3,6,4,5,7,6,4]

number = int(input("Enter the number which you want to find: "))

occured = occurence(items,number)

print(f"Occurence of {number} is {occured}")
