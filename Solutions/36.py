arr = [5,3,7, 2, 1]

acceding = 0
descending = 0


for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        descending = 1
    else:
        descending = 0
        break

for i in range(len(arr)-1):
    if arr[i] < arr[i+1]:
        acceding = 1
    else:
        acceding = 0
        break

if acceding or descending:
    if acceding:
        print("acceding")
    if descending:
        print("descending")
    print("Monotonic")

else:
    print("Not Monotonic")
