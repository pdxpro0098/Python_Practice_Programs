mat1 = [
    [5, 21],
    [9, 5],
    [2, 12]
]
mat2 = [
    [32, 5, 8],
    [4, 41, 45]
]

result = [[0 for j in range(3)] for i in range(3)] 

for i in range(3):
    for j in range(3):
        for k in range(2):
            result[i][j] += mat1[i][k] * mat2[k][j]
    
for row in result:
    print(row)