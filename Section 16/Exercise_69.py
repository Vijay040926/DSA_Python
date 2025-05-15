def find_missing_number(nums):
    n = len(nums)+1
    for i in range(0,n):
        if i not in nums:
            return i
nums = [3, 0, 1]
res=find_missing_number(nums)
print(res)