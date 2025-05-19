def sumNatural(a = [2,4,5,6,2]):
        result = 0
        for i in range(0,len(a)):
            result = result + a[i]
        return f"The sum of all Natural No is: {result}"

print(sumNatural(a = [2,4,5,6,2]))
