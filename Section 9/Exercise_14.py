def generate_hollow_inverted_right_angled_triangle(n):
    lst=[]
    for i in range(n,1,-1):
        if i==n:
            lst.append('*'*i)
        elif i<n:
            lst.append('*'+' '*(i-2)+'*')
    lst.append('*')
    return lst
res = generate_hollow_inverted_right_angled_triangle(4)
print(res)