def intersection(nums1,nums2):
    l = []
    for i in range(0,len(nums1)):
        for j in range(0, len(nums2)):
            if nums1[i] == nums2[j]:
                l.append(nums1[i])
    return list(set(l))
            # else:
            #     continue
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
res = intersection(nums1, nums2)
print(res)