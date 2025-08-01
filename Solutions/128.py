def squareOfDigit(n):
    if n>0:
        c = n % 10
        # print(c,"=",c**2)
        # squareOfDigit(n//10)
        return [c**2] + squareOfDigit(n//10)
    return []

n = 456
print("All Digits Squares:")
print(squareOfDigit(n))
