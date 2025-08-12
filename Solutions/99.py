def isLeapYear(n):
    if n % 100 == 0:
        return 0
    elif n % 400 == 0:
        return 1
    elif n % 4 == 0:
        return 1
    else:
        return 0

n = int(input("Enter the number: "))

if(isLeapYear(n) == 0):
    print(f"{n} isn't a leap year")
else:
    print(f"{n} is a leap year")




