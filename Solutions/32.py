def sumNatural(*a):
        result = 0
        for i in a:
            result += i
        return result
        

print(f"The sum of all Natural No is: {sumNatural(1,2,3,4,5)}")
