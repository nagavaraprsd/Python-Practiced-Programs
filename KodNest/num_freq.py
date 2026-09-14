nums=[2, 3, 2, 4, 3, 2, 5]
frequency={}
for value in nums:
    frequency[value]=0
for i in nums:
    frequency[i]+=1
for key,value in frequency.items():
    print(f"{key} ---> {value}")