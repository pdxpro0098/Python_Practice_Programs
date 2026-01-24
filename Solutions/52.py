# Krish's Approach
lst = [15, 61, 99, 39, 12, 34, 56, 78, 90]
print(sorted(lst)[-2])


# Dalip's Approach
def findSecondLargestNum(numbers):
    largest = second = float("-inf")
    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second


numbers = [3, 8, 5, 7]
print(f"Second largest number: {findSecondLargestNum(numbers)}")
