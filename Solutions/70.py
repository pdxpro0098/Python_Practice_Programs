# Krish's Approach
dictionary = {'a':1,'b':2,'c':3} 

keySum  = 0
for key,value in dictionary.items():
    keySum += value

print(keySum)

# Dalip's Approach
def sumOfAllDictElements(my_dict):
    sum = 0
    for num in my_dict.values():
        sum += num
    return sum

my_dict = {"dalip":3,"krish":2,"elon":1}

print(f"Sum of All Elements: {sumOfAllDictElements(my_dict)}")
    
