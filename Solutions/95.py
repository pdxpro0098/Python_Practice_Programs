# Krish's Approach
decimal_num = 10
binary_representation = bin(decimal_num)
print(binary_representation)


# Dalip's Approach
def decimalToBinary(n):
    b = []
    while n > 0:
        b.append(n % 2)
        n //= 2
    b.reverse()
    bc = int("".join(map(str, b)))
    return bc


number = 62

print(f"Binary of {number} is: {decimalToBinary(number)}")
