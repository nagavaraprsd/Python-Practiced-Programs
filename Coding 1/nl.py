records=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name,score])
scores=sorted({s[1] for s in records})
second_lowest = scores[1]
result=sorted(s[0] for s in records if s[1]==second_lowest)
print(result)