def linear_search(arr, target):
    if len(arr) == target:
        return False
    if target not in arr:
        return False
    return True
    return linear_search(arr[1:], target)


arr = [3, 5, 1, 7, 9]
target = 100
print(linear_search(arr, target))