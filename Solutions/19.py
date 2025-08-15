num = 370
numCp = num
power = len(str(num))
sum = 0

for i in range(power):
    ld_power = (num % 10) ** power
    sum += ld_power
    num //= 10

if sum==numCp:
    print("armstrong")
else:
    print("not armstrong")