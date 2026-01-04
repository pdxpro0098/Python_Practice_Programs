# Krish
import functools

n = 10
fib = functools.reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])

print(fib)


# Dalip(nikamma)
n = int(input("Enter the number: "))

fibonacci = [0,1]
[fibonacci.append(fibonacci[-1] + fibonacci[-2]) for _ in range(n-2)]
print(fibonacci)
