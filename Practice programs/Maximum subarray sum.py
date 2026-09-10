arr=[1,2,4,7,9]
target=11
seen=set()
lst=[]
compliment=0
for num in arr:
    compliment=target-num
    if compliment in seen:
        lst.append([num,compliment])
    seen.add(num)
print(lst)