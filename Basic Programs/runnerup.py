x=1
y=2
z=1
n=2
listof_x=[i for i in range(x+1)]
listof_y=[i for i in range(y+1)]
listof_z=[i for i in range(z+1)]
result=[]
result1=[]
for a in listof_x:
    for b in listof_y:
        for c in listof_z:
            result.append([a,b,c])
result1=result.copy()
for i in range(len(result) - 1, -1, -1):
    a, b, c = result[i]
    if a + b + c == n:
        result1.pop(i)
print(result1)
print(result)