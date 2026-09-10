tup=(1,2,5,7,9,2,5,9,8)
dict={}
for i in tup:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
print(tup[::-1])