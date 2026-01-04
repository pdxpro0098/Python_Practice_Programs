string = "1,2,3,4,5,6,7,8,9,10"
numbers_list = string.split(',')
product = 1
for num in numbers_list:
    product *= int(num)

print(product)