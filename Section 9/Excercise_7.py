def generate_inverted_pyramid(n):
    lst=[' '*(n-i)+'*'*(2*i-1)+' '*(n-i) for i in range(n,0,-1)]
    return lst
res = generate_inverted_pyramid(3)
print(res)
