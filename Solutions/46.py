num = 20
numCp = num
harshadNumber = 0

while numCp != 0:
    harshadNumber += numCp % 10
    numCp //= 10

if num % harshadNumber == 0:
    print(num, "is Harshad number")
else:
    print(num, "is not Harshad number")
