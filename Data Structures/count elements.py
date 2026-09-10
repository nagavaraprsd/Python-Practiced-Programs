nums=[1,2,3,3,4,3,5,2,6,7,8,9,8,7,8,9]
dict={}
for i in nums:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)