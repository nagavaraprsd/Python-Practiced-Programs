arr=[1,2,3,4,2,1,5,3]
freq={}
a=[]
for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
for k,v in freq.items():
    if v>1:
        a.append(k)
print(a)