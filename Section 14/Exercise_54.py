def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
arr = [1,2,3,4,5]
target = 3
res = linear_search(arr, target)
print(res)