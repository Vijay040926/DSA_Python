def generate_right_angled_triangle(n):
    lst=[' '*(n-i)+'*'*(i) for i in range(1,n+1)]
    return lst
res = generate_right_angled_triangle(3)
print(res)