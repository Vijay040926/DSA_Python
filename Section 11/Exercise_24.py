def check_unique(lst):
    l=[]
    for i in lst:
        if i not in l:
            l.append(i)
    if l==lst:
        return True
    else:
        return False
lst=[1,2,3,4,5]
res = check_unique(lst)
print(res)