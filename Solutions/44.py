happyNumber = 13
lst = list()
power = len(str(happyNumber))
def powerSum(num, power):
    sum = 0
    while num != 0:
        ld = num % 10
        sum += ld**power
        num //= 10
    return sum
sum = powerSum(happyNumber, power)
while sum not in lst:
    if sum == 1:
        print("Happy number", happyNumber)
        break
    lst.append(sum)
    sum = powerSum(sum, power)
