def countNegatives(grid):
    n = len(grid)
    count = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] < 0:
                count+=1
    return count
grid =  [[4, 3, 2, 1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
res = countNegatives(grid)
print(res)