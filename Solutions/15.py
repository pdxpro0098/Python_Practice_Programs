def prime(num):
    isPrime = 1
    for i in range(2, num):
        if num % i == 0:
            isPrime = 0
            break
    return isPrime

for i in range(1,10):
    if prime(i):
        print(i)

num: int = 0
num = "from"

print(num)