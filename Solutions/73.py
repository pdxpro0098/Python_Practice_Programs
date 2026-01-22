# Krish's Approach
import math

numbers = input("Provide D: ")
numbers = numbers.split(',')

result_list = []
for D in numbers:
    Q = round(math.sqrt(2 * 50 * int(D) / 30))
    result_list.append(Q)

print(result_list)

# Dalip's Approach
import math
numbers = list(input("Enter the values(C ,D ,H): ").split(","))
# num = [int(ch) for ch in numbers]
c,d,h = map(int,numbers)

# Q = (sqrt((2*C*D)/H))3,
#An algebric formula

def qComputing(c,d,h):
    Q = (2*c*d)/h
    return math.sqrt(Q)

print(round(qComputing(c,d,h),2))

