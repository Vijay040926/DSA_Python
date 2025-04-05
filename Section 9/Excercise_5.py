def generate_inverted_triangle(n):
    lst=['*'*i for i in range(n,0,-1)]
    return lst
res = generate_inverted_triangle(3)
print(res)