nums = [4, 5, 1, 2, 1, 4, 5, 2, 8]
dict1={}
for value in nums:
    dict1[value]=0
for i in nums:
    dict1[i]+=1
for i in nums:
    if dict1[i] == 1:
        print(i)
        break