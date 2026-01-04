def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i

n = int(input("Enter the number: "))
print(factorial(n))