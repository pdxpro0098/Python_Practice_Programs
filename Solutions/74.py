# Krish's Approach
lst = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]


for i in range(3):
    for j in range(3):
        lst[i][j] = i*j

print(lst)

# Dalip's Approach
rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(i*j)
    matrix.append(row)

for row in matrix:
    for val in row:
        print(val, end=" ")
    print()
