dict1={}
keys=list(input("Enter the keys\n").split())
values=list(map(int,input("Enter the Values\n").split()))
for i in range(len(keys)):  # or dict1=dict(zip(keys,values))
    dict1[keys[i]]=values[i] 
print(dict1)
