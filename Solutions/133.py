b = 10010110010


def countSetBit(number):
    setBit = 0
    for digit in str(number):
        if digit == "1":
            setBit += 1
    return setBit


print(countSetBit(b))