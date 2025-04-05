def generate_pyramid(n):
    lst=[' '*(n-i)+'*'*(2*i-1)+' '*(n-i) for i in range(1,n+1)]
    return lst
res = generate_pyramid(3)
print(res)