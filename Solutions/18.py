#Global variables
a = 0
b = 1

def fibonacci(n):
    #Local variables
    a = 0
    b = 1

    for i in range(1, n+1):
        print(a, end=" ")
        c = a + b  # Store a = 0 + b = 1
        a = b  # a = 1
        b = c  # b =  1


fibonacci(8)
