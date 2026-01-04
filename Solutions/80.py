# 80. Write a Python Program to generate numbers divisible by 7 using a generator.

# krish's Approach
def generator():
    for i in range(1, 1000):
        yield i*7


gen = generator()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


# Dalip's Approach
def divisible(limit):
    for i in range(5,limit):
        if i % 7 == 0:
            yield i


for num in divisible(50):
    print(num)
