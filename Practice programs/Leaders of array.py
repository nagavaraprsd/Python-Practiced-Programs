arr=[16,17,4,3,5,2]
leaders=[]
for i in range(len(arr)):
    leader=True
    for j in range(i+1,len(arr)):
        if arr[j]>arr[i]:
            leader=False
            break
    if leader:
        leaders.append(arr[i])
print(leaders)