def reverseString(n, length):
    name_list = list(n)
    start = 0
    end = length - 1
    while start <= end:
        name_list[start], name_list[end] = name_list[end], name_list[start]
        start += 1
        end -= 1
    return "".join(name_list)


name = input("Enter the string: ")

length = len(name)

reverse_string = reverseString(name, length)

if reverse_string == name:
    print(f"{name} is Palindrome")
else:
    print(f"{name} isn't Palindrome")

