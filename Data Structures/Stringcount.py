#String=list(map(str,input().split()))
String=list(input())
dict1={}
for value in String:
    dict1[value]=0
for i in String:
    dict1[i]+=1
print(dict1)