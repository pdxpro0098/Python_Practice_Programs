arr = [1, 2, 3, 4, 5, 6, 7]

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
        print("acceding",end=" ")
    if descending:
        print("descending",end=" ")
    print("Monotonic")

else:
    print("Not Monotonic")
