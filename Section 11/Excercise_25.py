def reverse_list(lst):
    n=len(lst)
    l=[]
    for i in range(n-1,-1,-1):
        l.append(lst[i])
    return l
lst=[1,2,3,4,5]
res = reverse_list(lst)
print(res)