a = 0
b = 1
n = int(input("Enter the number: "))

for i in range(1,n+1):
    print(a)
    c = a + b
    a = b
    b = c 
