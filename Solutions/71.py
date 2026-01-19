# Krish's Approach
dictionary = {'a': 1, 'b': 2, 'c': 3}

keySum = 1
for key, value in dictionary.items():
    keySum *= value

print(keySum)

# Dalip's Approach
def ProdOfAllDictElements(my_dict):
    product = 1
    for num in my_dict.values():
        product *= num
    return product

my_dict = {"dalip":4,"krish":3,"elon":2}

print(f"Product of All Elements: {ProdOfAllDictElements(my_dict)}")
    
