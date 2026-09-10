num=int(input())
total=0
tempo=[]
for i in str(num):
    tempo.append(i)
for i in tempo:
    total+=int(i)*int(i)*int(i)
if total==num:
    print("Arm Strong")
else:
    print("Not Armstrong")