arr1=[1,2,3,4,5,6]
arr2=[5,6,7,8,9,10]
i_s=[]
for i in arr1:
    for j in arr2:
        if i==j:
            i_s.append(i)
print(i_s)