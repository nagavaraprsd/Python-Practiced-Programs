num=input()
num=str(num)
nums=[]
n=len(num)
for i in range(n-1,-1,-1):
    nums.append(num[i])
    if i==-1:
        break
print(nums)
s="".join(nums)
print(s)
