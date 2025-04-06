def gcd(n,m):
    c = 1
    if m<n:
        t = m
        m = n
        n = t
    while c>0:
        c = m%n
        m = n
        n = c
        continue
    return m
res = gcd(48, 18)
print(res)