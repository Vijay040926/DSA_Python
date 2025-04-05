def max_consecutive_difference(lst):
    l=[];m=0;large=float('-inf')
    if lst==[]:
        return 0
    else:
        for i in range(len(lst)-1):
            m = abs(lst[i]-lst[i+1])
            l.append(m)
        for i in l:
            large = max(i,large)
    return large
lst=[]
res = max_consecutive_difference(lst)
print(res)