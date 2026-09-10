n=int(input("Enter the number you want to find the Factorial to\n"))
total=1
a=[]
for i in range(1,n+1):
    total*=i
    #print(total)
    a.append(total)
print(total)
print(a)