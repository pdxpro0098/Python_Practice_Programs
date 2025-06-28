def isPionic(num):
    for i in range(num):
        if num == (i*(i+1)):
            return 1
    return 0

for i in range(1,101):
    if isPionic(i):
        print(i)