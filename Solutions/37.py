mat1 = [[8,6,4],
        [5,7,2],
        [1,3,9]]
mat2 = [[2,4,6],
        [5,3,8],
        [9,7,1]]

# Createing empty result matrix
result = [[0 for j in range(3)] for i in range(3)]

for i in range(3):
    for j in range(3):
        result[i][j] = mat1[i][j] + mat2[i][j]


for i in range(3):
    for j in range(3):
        print(result[i][j],end=" ")
    print()
