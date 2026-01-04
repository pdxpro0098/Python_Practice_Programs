# Krish's Approach
def mean(nums):
    lst = [int(digit) for digit in str(nums)]
    m = 0
    c = 0
    for num in lst:
        c += 1
        m += (num)
    return m / c

digit = 4444
print(mean(digit))


# Dalip's Approach
digit = 352
def findMean(digit):
    addition = 0
    count = 0
    while(digit>0):
        c = digit %10
        count +=1
        addition += c
        digit //= 10

    return addition / count

print("Mean:",format(findMean(digit),".2f"))

