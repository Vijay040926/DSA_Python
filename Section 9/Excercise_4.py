def generate_triangle(n):
    lst = ['*' * i for i in range(1, n + 1)]
    return lst


res = generate_triangle(3)
print(res)
