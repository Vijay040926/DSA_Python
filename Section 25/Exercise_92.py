def recursive_sum(arr):
    if len(arr) == 0:
        return 0
    return recursive_sum(arr[1:]) + arr[0]


print(recursive_sum([1, 2, 3, 4, 5]))