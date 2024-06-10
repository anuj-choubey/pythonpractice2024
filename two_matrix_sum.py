rows = 2
cols = 3

matrix1 =[
        [1,2,3],
        [4,5,6]
]
matrix2 = [
                [7,8,9],
                [10,11,12]
            ]

result  = [[0 for _ in range (cols)]for _ in range (rows)]

for i in range (rows):
    for j in range (cols):
        result[i][j] = matrix1[i][j] + matrix2[i][j]
print(result)
