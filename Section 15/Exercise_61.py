def findMin(nums):
    min = nums[0]
    for i in range(1, len(nums)):
        if min > nums[i]:
            min = nums[i]

    return min

nums = [4, 5, 6, 7, 0, 1, 2]
res = findMin(nums)
print(res)