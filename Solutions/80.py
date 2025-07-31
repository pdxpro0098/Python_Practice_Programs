# 80. Write a Python Program to generate numbers divisible by 7 using a generator.

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
