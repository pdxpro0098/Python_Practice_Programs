def countVowels(text):
    vowels = "aeiou"  
    count = 0
    for char in text:
        if char.lower() in vowels:
            count += 1
    return count


string = "✅ 121. Write a Python Program to count the vowels in a string."
print(countVowels(string))
