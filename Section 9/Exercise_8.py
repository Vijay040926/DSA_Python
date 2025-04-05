def generate_number_triangle(n):
    lst=[f"{i}"*i for i in range(1,n+1)]
    return lst
res = generate_number_triangle(3)
print(res)