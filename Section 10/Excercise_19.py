def calculate_lift_rounds(n,capacity):
    r=0
    for i in range(n):
        n=n-capacity
        if n>0:
            r=r+1
        else:
            return r+1
    # return r
res = calculate_lift_rounds(10,3)
print(res)