def generate_floyds_triangle(n):
    lst=[]
    num = 1
    for i in range(1,n+1):
        row = " ".join(str(num+j) for j in range(i))
        lst.append(row)
        num +=i
    return lst
res = generate_floyds_triangle(3)
print(res)