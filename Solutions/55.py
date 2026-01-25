# Krish's Approach
lst = [12, 23, 56, 78, 91]


def printEven(lst):
    for item in lst:
        if item % 2 != 0:
            print(item)


printEven(lst)


# Dalip's Approach
def fetchOddNo(num):
    evenNumbers = []
    for i in numbers:
        if i % 2 != 0:
            evenNumbers.append(i)
    return evenNumbers


numbers = [3, 2, 4, 8, 9, 13]

print(f"Odd no: {fetchOddNo(numbers)}")
