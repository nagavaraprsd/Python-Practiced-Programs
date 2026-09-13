nums=[4, 5, 6, 4, 5, 4, 6, 6, 6, 7]
dict1={}
Sec_Lar=0
for value in nums:
    dict1[value]=0
for i in nums:
    dict1[i]+=1
freqs=list(dict1.values())
freq=sorted(freqs,reverse=True)
print(f"Second Largest Frequency : {freq[1]} ")


