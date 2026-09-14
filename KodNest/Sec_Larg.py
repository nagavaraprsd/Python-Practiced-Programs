# nums1=[10, 5, 20, 8, 20, 15]
# nums=list(set(nums1))
# sec_larg=0
# larg=0
# for i in range(0,len(nums)):
#     if nums[i]>larg:
#         sec_larg=larg
#         larg=nums[i]
        
#     elif nums[i]>sec_larg:
#         sec_larg=nums[i]
# print(larg)
# print(sec_larg)
# print(nums)

# or 

nums1=[10, 5, 20, 8, 20, 15]
nums=list(set(nums1))
largest=max(nums)
sec_largest=nums[0]
for i in range(1,len(nums)-1):
    if nums[i]<largest and sec_largest<nums[i]:
        sec_largest=nums[i]
print(sec_largest)
print(largest)