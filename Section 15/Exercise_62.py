def search(nums,target):
    for i in range(0,len(nums)):
        if nums[i] == target:
            return i
    return -1
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
res = search(nums,target)
print(res)