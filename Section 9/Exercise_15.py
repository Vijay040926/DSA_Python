def generate_number_pyramid(n):
    lst=[]
    for i in range(1,n+1):
        spaces = ' '*(n-i)
        nums = ' '.join(str(j) for j in range(1,i+1))
        lst.append(spaces+nums+spaces)
    return lst
res = generate_number_pyramid(4)
print(res)