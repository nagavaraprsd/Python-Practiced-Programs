s="I told him that that 'that' that that editor had deleted was not that that that I had marked"
lst=list(s.split())
dict1={}
for i in lst:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1
print(dict1)