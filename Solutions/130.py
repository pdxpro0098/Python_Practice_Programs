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
