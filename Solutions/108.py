lst = [2, 3, 7, 1,  8, 9, 10, 4, 5, 6,]

def maxProduct(lst):
    sort = sorted(lst)
    return sort[-1] * sort[-2]

print(maxProduct(lst))