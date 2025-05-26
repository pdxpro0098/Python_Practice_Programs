num_1 = 120
num_2 = 16

grater = num_1 if num_1 > num_2 else num_2
hcf = None
for i in range(grater, 1, -1):
    if num_1 % i == 0 and num_2 % i == 0:
        hcf = i
        break
    
print(hcf)