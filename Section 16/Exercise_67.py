def rotate_left(ARR,D):
    if ARR==[]:
        return ARR
    else:
        n=len(ARR)-1
        for i in range(0,D):
            last=ARR[0]
            for j in range(0,n):
                ARR[j]=ARR[j+1]
            ARR[n]=last
        return ARR
ARR = [10, 20, 30, 40, 50]
D=3
res = rotate_left(ARR,D)
print(res)