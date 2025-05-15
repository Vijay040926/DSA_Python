def can_be_rotated(mat, target):
    res = [''.join(str(num) for num in row) for row in target]
    result = ''.join(str(int(i, 2)) for i in res)

    org = [''.join(str(num) for num in row) for row in mat]
    og = ''.join(str(int(i, 2)) for i in org)
    if og == result[::-1]:
        return True
    return False


mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
target = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
res = can_be_rotated(mat, target)
print(res)