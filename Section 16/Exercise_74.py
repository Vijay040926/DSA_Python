def max_subarray_sum(arr):
    current_sum = 0
    max_sum = float('-inf')

    if arr == []:
        return 0
    else:
        for i in arr:
            current_sum += i
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0
        return max_sum


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
res = max_subarray_sum(arr)
print(res)