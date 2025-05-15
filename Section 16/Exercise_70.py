def is_sorted(arr):
    for i in  range(0,len(arr)-1):
        if arr[i]>arr[i+1] :
            return False
    return True
arr = [1, 3, 2, 4, 5]
res = is_sorted(arr)
print(res)