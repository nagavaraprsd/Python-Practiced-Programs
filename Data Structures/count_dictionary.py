nums=[1,2,3,2,4,2,1,5,5,6]
dict1={}
for value in nums:
    dict1[value]=0
for i in nums:
    dict1[i]+=1
#to print keys and Valyes in pairs
for i,j in dict1.items():
    print(i,":",j)
print(dict1)
#Largest and Smallest values
print("Largest value",max(dict1.values()))
print("Smallest value",min(dict1.values()))
#Merging Dictionaries
dict2={20: 2, 25: 3, 30: 1, 40: 4}
for i,j in dict2.items():
    dict1[i]=j
print(dict1)
#reverse the Keys and values
dict3={}
for k,v in dict2.items():
    dict3[v]=k
print(dict3)
