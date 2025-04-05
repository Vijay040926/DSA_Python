def calculate_y(slope, intercept, x):
    y = float((slope*x) + intercept)
    return y
res = calculate_y(2,3,4)
print(res)