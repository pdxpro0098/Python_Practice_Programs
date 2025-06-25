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