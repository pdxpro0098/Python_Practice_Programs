# Dalip's Approach
# formula for Curzon Number:
#  2^N+1 / 2xN+1
def isCurzon(n):
    numerator = (2**n) + 1
    denominator = (2*n) + 1
    return numerator % denominator == 0


n = int(input("Enter the number: "))

if isCurzon(n):
    print(f"{n} is a Curzon Number.")
else:
    print(f"{n} isn't a Curzon Number.")


