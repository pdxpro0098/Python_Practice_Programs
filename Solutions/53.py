# Krish's Approach

lst = [121, 2, 34, 65, 81, 45, 31, 92, 69, 11]


def nthLargest(num, list):
    if num > len(list):
        return -1
    return sorted(lst)[num - 1]


print(nthLargest(3, lst))


# Dalip's Approach
numbers = [3, 2, 5, 7]
numbers.sort(reverse=True)

n = int(input("Enter the nth largest number: "))

print(f"{n} largest element: {numbers[n-1]}")

# # Dalip's Approach
# numbers = [3, 8, 5, 7]


# def findSecondLargestNum(numbers):
#     largest = second = float("-inf")
#     for num in numbers:
#         if num > largest:
#             second = largest
#             largest = num
#         elif num > second and num != largest:
#             second = num
#     return second


# print(f"Second largest number: {findSecondLargestNum(numbers)}")

