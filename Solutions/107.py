# Dalip's Approach
array = [3, 8, 2, 9, 1]
maxSum = 0
for i in range(0, len(array)):
    for j in range(i + 1, len(array)):
        if array[i] * array[j] > maxSum:
            maxSum = array[i] * array[j]
print(f"Max Product of Two Integer:", maxSum)
