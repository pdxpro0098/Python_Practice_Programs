def evenNumbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i


for num in evenNumbers(20):
    print(num)
