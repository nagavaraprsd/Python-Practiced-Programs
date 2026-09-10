s="NagavaraPrasa"
sb="ra"
count=0
for i in range(len(s)-len(sb)+1): #or range(len(s))
    if s[i:i+len(sb)]==sb:
        count+=1
print(count)