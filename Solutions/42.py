# Krish's Approach
def isDisarium(number):
    n = number
    isDisarium = 0
    power = len(str(number))
    while number != 0:
        ld = number % 10
        isDisarium += ld**power
        power -= 1
        number //= 10
    return 1 if isDisarium == n else 0

print(isDisarium(135))


# Dalip's Approach
def isDisarium(n):
    num_str = str(n)
    result = 0
    for i in range(len(str(n))):
        digit = int(num_str[i])
        result += pow(digit,i+1) 
    return "Disarium" if result == n else "Not Disarium"

print(isDisarium(89))


