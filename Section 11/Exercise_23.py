def remove_duplicates(lst):
    return list(set(lst))
lst = [1, 2, 2, 3, 4, 4, 5]
res= remove_duplicates(lst)
print(res)