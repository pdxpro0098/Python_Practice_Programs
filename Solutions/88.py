# Krish's Approach

import functools

n = 10
fib = functools.reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])

print(fib)


# Dalip's Approach
n = 10

fib_list = [0, 1]
[_ for _ in range(2, n) if fib_list.append(fib_list[-1] + fib_list[-2])]
print(fib_list)
