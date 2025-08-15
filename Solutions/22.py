def HCF(num1, num2):
    grater = num1 if num1 > num2 else num2
    hcf = None
    for i in range(grater, 1, -1):
        if num1 % i == 0 and num2 % i == 0:
            hcf = i
            break
    return hcf

num_1 = 120
num_2 = 16
print(HCF(num_1, num_2))