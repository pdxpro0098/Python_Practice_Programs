def DecimalToBinaryConverter(num):
    binary = list()
    while num != 0:
        binary.append(num % 2)
        num //= 2
    binary.reverse()

    print("Binary", binary)


def DecimalToOctalConverter(num):
    octal = list()
    while num != 0:
        octal.append(num % 8)
        num //= 8
    octal.reverse()
    print("Octal", octal)


def DecimalToHexadecimalConverter(num):

    hex = list()
    hexadecimal = list()

    while num != 0:
        hex.append(num % 16)
        num //= 16
    hex.reverse()

    for num in hex:
        if num == 10:
            hexadecimal.append("A")
        elif num == 11:
            hexadecimal.append("B")
        elif num == 12:
            hexadecimal.append("C")
        elif num == 13:
            hexadecimal.append("D")
        elif num == 14:
            hexadecimal.append("E")
        elif num == 15:
            hexadecimal.append("F")
        else:
            hexadecimal.append(num)

    print("Hexadecimal", hexadecimal)


num = 3
DecimalToBinaryConverter(num)

DecimalToOctalConverter(num)

DecimalToHexadecimalConverter(num)