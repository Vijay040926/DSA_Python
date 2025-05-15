def bubble_sort(lst):
    size = len(lst)
    for i in range(0,size):
        for j in range(0,size-1):
            if lst[j] > lst[j+1]:
                t = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = t
    return lst
lst = [5,4,3,2,1]
res = bubble_sort(lst)
print(res)