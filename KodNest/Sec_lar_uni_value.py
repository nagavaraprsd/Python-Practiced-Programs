nums1 = [10, 5, 8, 20, 15, 20, 3]
nums = list(set(nums1))
largest=nums[0]
sec_largest=nums[0]
for i in nums:
    if i>largest:
        sec_largest=largest
        largest=i
    elif i>sec_largest:
        sec_largest=i
print(largest)
print(sec_largest)
