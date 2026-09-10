num=int(input("Enter a number\n"))
n=len(str(num))
num1=list(map(int,str(num)))
num2=[]
total=0
for i in range(0,n):
    num2.append(num1[i]**n)
for j in range(0,n):
    total+=num2[j]
if num==total:
    print(f" The number '{num}' is an Armstrong Number")
else:
    print(f"The number '{num}' is not an Armstrong Number")