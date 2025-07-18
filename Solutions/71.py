dictionary = {'a': 1, 'b': 2, 'c': 3}

keySum = 1
for key, value in dictionary.items():
    keySum *= value

print(keySum)
