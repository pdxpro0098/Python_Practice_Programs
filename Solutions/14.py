n = int(input("Enter the number: "))
def primeNoCheck(n):
    count = 0
    for i in range(2,n+1):
        if n % i == 0:
            count = count + 1
    if count == 1:
        print("Prime Number")
    else:
        print("Not Prime Number")

primeNoCheck(n)