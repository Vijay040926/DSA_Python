def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    rows = len(matrix);
    cols = len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        row = mid // cols
        col = mid % cols
        mid_value = matrix[row][col]

        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
res = search_matrix(matrix, target)
print(res)

# apply binary search as if it were a 1D array