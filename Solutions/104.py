def factorial(n):
    if(n>0):
        n*= factorial(n-1)
        return n
    return 0


print(factorial(5))