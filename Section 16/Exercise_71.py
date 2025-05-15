def move_zeroes(nums):
    num = []
    while 0 in nums:
        nums.remove(0)
        num.append(0)
    nums.extend(num)
    return nums
nums = [0, 1, 0, 3, 12]
res = move_zeroes(nums)
print(res)