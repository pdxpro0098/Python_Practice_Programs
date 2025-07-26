string = """
 68. Write a Python Program to sort a dictionary by key. 69. Write a Python Program to sort a dictionary by value. 70. Write a Python Program to sum all the items in a dictionary. 71. Write a Python Program to multiply all the items in a dictionary. 72. Write a Python Program to remove a key from a dictionary.73. Write a Python Program to calculate Q = √[(2 * C * D)/H] with values provided as comma-separated input. 74. Write a Python Program to generate a 2D array where the element value is i*j. 75. Write a Python Program to sort a comma-separated sequence of words alphabetically. 76. Write a Python Program to remove duplicate words and sort them alphanumerically. 77. Write a Python Program to count the number of each character in a string. 78. Write a Python Program to count letters and digits in a sentence.79. Write a Python Program to check password validity based on multiple conditions.80. Write a Python Program to generate numbers divisible by 7 using a generator.81. Write a Python Program to calculate bank account net amount from transaction log.82. Write a Python Program to sort a list of tuples based on the second element.83. Write a Python Program to count frequency of words in a given line of text.84. Write a Python Program to compress and decompress a string using zlib.

"""
char = 0
digit = 0

for c in string:
    if c.isalpha():
        char += 1
    elif c.isdigit():
        digit += 1

print(char)
print(digit)
