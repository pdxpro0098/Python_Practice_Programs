def divisibles():
    for i in range(5, 100):
        if i % 7 == 0 and i % 5 == 0:
            yield i


for num in divisibles():
    print(num)
