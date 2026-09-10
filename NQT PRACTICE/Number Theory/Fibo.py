n=int(input("Enter n"))
nums=[0,1]
temp=0
for i in nums:
    temp=nums[-1]+nums[-2]
    nums.append(temp)
    if len(nums)==n:
        break
print(nums)