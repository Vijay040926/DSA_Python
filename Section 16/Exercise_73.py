def find_max_consecutive_ones(nums):
    max_count = 0
    current_count = 0
    for num in nums:
        if num == 1:
            current_count += 1
        else:
            max_count = max(max_count, current_count)
            current_count = 0
    return max(max_count, current_count)
nums = [1, 1, 0, 1, 1, 1]
res = find_max_consecutive_ones(nums)
print(res)