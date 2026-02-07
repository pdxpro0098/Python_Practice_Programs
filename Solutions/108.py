# Krish's Approach
lst = [
    2,
    3,
    7,
    1,
    8,
    9,
    10,
    4,
    5,
    6,
]


def maxProduct(lst):
    sort = sorted(lst)
    return sort[-1] * sort[-2]


print(maxProduct(lst))

# Dalip's Approach
array = [3, 8, 2, 9, 1]
maxSum = 0
for i in range(0, len(array)):
    for j in range(i + 1, len(array)):
        if array[i] * array[j] > maxSum:
            maxSum = array[i] * array[j]
print(f"Max Product of Two Integer:", maxSum)
