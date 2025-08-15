sentence = "Write a Python Program to count occurrences of each word in a sentence Write a Python Program to find area of a hexagon. Write a Python Program to convert decimal number to binary. Write a Python Program to convert snake_case to camelCase. Write a Python Program to check if a year is a leap year.  Write a Python Program to create a class and display its attributes.  Write a Python Program to define a Circle class with area and perimeter methods.  Write a Python Program to implement a simple calculator using classes.  Write a Python Program to move all elements of one type to the end of a list."
sentenceList = sentence.lower().split(" ")
lstMap = dict()

for val in sentenceList:
    if val not in lstMap:
        lstMap[val] = 1
    else:
        lstMap[val] += 1

print(lstMap)