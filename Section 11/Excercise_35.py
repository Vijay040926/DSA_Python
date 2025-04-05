def is_subset(lst1, lst2):
    n=len(lst1)
    i=0
    count=0
    while i<n:
        if lst1[i]==lst2[i]:
            count += 1
        else:
            count = 0
        i=i+1
    if count==len(lst1):
        return True
    else:
        return False
lst1=[1,2,3]
lst2=[1,2,3,4,5]
res = is_subset(lst1, lst2)
print(res)

#ALternative code
def is_subset(lst1, lst2):

    for i in lst1:

        if i not in lst2:

            return False

    return True