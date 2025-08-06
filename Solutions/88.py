n = int(input("Enter the number: "))

fibonacci = [0,1]
[fibonacci.append(fibonacci[-1] + fibonacci[-2]) for _ in range(n-2)]
print(fibonacci)
