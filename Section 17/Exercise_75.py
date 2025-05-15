def generate(numRows):
    triangle = []

    for i in range(numRows):
        row = [1]  # First element is always 1
        if triangle:
            last_row = triangle[-1]
            for j in range(1, i):
                row.append(last_row[j - 1] + last_row[j])
            row.append(1)  # Last element is always 1
        triangle.append(row)

    return triangle
numRows = 3
res = generate(numRows)
print(res)