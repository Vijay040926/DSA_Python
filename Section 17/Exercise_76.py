def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
def display_result(matrix):
    rotate(matrix)
    for row in matrix:
        print(row)
matrix = [[1, 2, 3],[4, 5, 6],[7,8, 9]]
res = display_result(matrix)
print(res)