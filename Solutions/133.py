# krish's Approach
b = 10010110010


def countSetBit(number):
    setBit = 0
    for digit in str(number):
        if digit == "1":
            setBit += 1
    return setBit


print(countSetBit(b))


# Dalip's Approach

def decimalToBinary(decimalNum):
    power = 1
    ans = 0
    while(decimalNum > 0):
        remainder = decimalNum % 2 
        decimalNum //= 2
        ans += (remainder*power)
        power = power * 10
    return ans



def countSetBits(n):
    count = 0
    while(n>0):
        c = n % 10
        if(c == 1):
            count += 1
        n//=10
    return count

print(f"Set bits: {countSetBits(decimalToBinary(15))}")
