def matrix_reshape(mat, r, c):
    m = len(mat)
    n = len(mat[0])
    if m * n != r * c:
        return mat

    flat_list = []
    for row in mat:
        for num in row:
            flat_list.append(num)
    reshaped_matrix = []
    for i in range(r):
        reshaped_matrix.append(flat_list[i * c: (i + 1) * c])
    return reshaped_matrix


def display_reshaped_matrix(mat, r, c):
    result = matrix_reshape(mat, r, c)
    for row in result:
        print(row)


mat = [[1, 2], [3, 4]]
r, c = 1, 4
display_reshaped_matrix(mat, r, c)