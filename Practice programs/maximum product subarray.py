arr=[2,4,3,6,8,12]
target=12
seen=set()
pairs=[]
pair=0
for i in arr:
    pair=target//i
    if pair in seen:
        pairs.append([i,pair])
    seen.add(i)
print(pairs)