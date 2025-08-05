def binarySearch(items, target):
    start = 0
    end = len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if target > items[mid]:
            start = mid + 1

        elif target < items[mid]:
            end = mid - 1
        else:
            return mid

    return -1


items = [1, 3, 5, 6, 7, 8, 9]



target = int(input("Enter the target:"))

result = binarySearch(items, target)

if result != -1:
    print(f"Element {target} found at Index: {result}")
else:
    print(f"Element {target} Not Found!")
