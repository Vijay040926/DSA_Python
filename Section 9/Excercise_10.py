def generate_diamond(n):
    lst=[' '*(n-i)+'*'*(2*i-1)+' '*(n-i) for i in range(1,n+1)]
    for i in range(n-1,0,-1):
        lst.append(' '*(n-i)+'*'*(2*i-1)+' '*(n-i))
    return lst
res = generate_diamond(3)
print(res)