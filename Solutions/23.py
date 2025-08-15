def LCM(num1, num2):

    def HCF(num1, num2):
        grater = num1 if num1 > num2 else num2
        for i in range(grater, 1, -1):
            if num1 % i == 0 and num2 % i == 0:
                return i

    return (num1*num2)//HCF(num1, num2)


num_1 = 120
num_2 = 16

print(LCM(num_1, num_2))