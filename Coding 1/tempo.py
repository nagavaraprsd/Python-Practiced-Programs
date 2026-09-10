num=input()
num=str(num)
nums=[]
n=len(num)
for i in range(0,n):
    nums.append(num[-i])
    i=i-1
    if i==-1:
        break
print(nums)