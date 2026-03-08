numbers = [8,9,3,5,6,12]
sum = 0
for i in numbers:
    if i % 2 == 0:
        sum+=i
print(f"Sum of all Even Elements: {sum}")