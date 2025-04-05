def merge_two_sorted_lists(list1,list2):
    if list1==[]:
        return list2
    else:
        l = sorted(list1+list2)
        return l
list1=[1,3,5]
list2=[2,4,6]
res= merge_two_sorted_lists(list1,list2)
print(res)