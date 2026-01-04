def mulitplyDigit(n):
    result = 1
    while n>0:
        result *= n % 10
        n //= 10
    return result

print(mulitplyDigit(533))
