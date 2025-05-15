def sum_of_elements(lst):
    sum = 0
    for i in range(0,len(lst)):
        sum += lst[i]
    return sum
lst = [-1, -2, -3, -4]
res = sum_of_elements(lst)
print(res)