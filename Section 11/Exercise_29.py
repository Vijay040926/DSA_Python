def rotate_list(lst,k):
    # n=len(lst)-1;last=lst[n]
    if lst==[]:
        return lst
    else:
        n=len(lst)-1;last=lst[n]
        for i in range(0,k):
            last=lst[n]
            for j in range(n,-1,-1):
                lst[j]=lst[j-1]
            lst[0]=last
        return lst
lst = [1,2,3,4,5]
k=2
res = rotate_list(lst,k)
print(res)